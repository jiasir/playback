from fabric.api import *
from fabric.contrib import files
from fabric.tasks import Task
from fabric.network import disconnect_all
from fabric.colors import red
import os
import argparse
import sys
from playback.cli import cli_description
from playback import __version__

parser = argparse.ArgumentParser(description=cli_description+'this command used for provision Nova Compute')
parser.add_argument('-v', '--version',
                   action='version',
                   version=__version__)
parser.add_argument('--user', 
                    help='the target user', 
                    action='store', 
                    default='ubuntu', 
                    dest='user')
parser.add_argument('--hosts', 
                    help='the target address', 
                    action='store', 
                    dest='hosts')

subparsers = parser.add_subparsers(dest='subparser_name')
install = subparsers.add_parser('install',
                                help='install nova compute')
install.add_argument('--my-ip',
                    help='the host management ip',
                    action='store',
                    default=None,
                    dest='my_ip')
install.add_argument('--rabbit-hosts',
                    help='rabbit hosts e.g. CONTROLLER1,CONTROLLER2',
                    action='store',
                    default=None,
                    dest='rabbit_hosts')
install.add_argument('--rabbit-pass',
                    help='the password for rabbit openstack user',
                    action='store',
                    default=None,
                    dest='rabbit_pass')
install.add_argument('--auth-uri',
                    help='keystone internal endpoint e.g. http://CONTROLLER_VIP:5000',
                    action='store',
                    default=None,
                    dest='auth_uri')
install.add_argument('--auth-url',
                    help='keystone admin endpoint e.g. http://CONTROLLER_VIP:35357',
                    action='store',
                    default=None,
                    dest='auth_url')
install.add_argument('--nova-pass',
                    help='passowrd for nova user',
                    action='store',
                    default=None,
                    dest='nova_pass')
install.add_argument('--novncproxy-base-url',
                    help='nova vnc proxy base url e.g. http://CONTROLLER_VIP:6080/vnc_auto.html',
                    action='store',
                    default=None,
                    dest='novncproxy_base_url')
install.add_argument('--glance-host',
                    help='glance host e.g. CONTROLLER_VIP',
                    action='store',
                    default=None,
                    dest='glance_host')
install.add_argument('--neutron-endpoint',
                    help='neutron endpoint e.g. http://CONTROLLER_VIP:9696',
                    action='store',
                    default=None,
                    dest='neutron_endpoint')
install.add_argument('--neutron-pass',
                    help='the password for neutron user',
                    action='store',
                    default=None,
                    dest='neutron_pass')
install.add_argument('--rbd-secret-uuid',
                    help='ceph rbd secret for nova libvirt',
                    action='store',
                    default=None,
                    dest='rbd_secret_uuid')

args = parser.parse_args()

conf_nova_conf = """[DEFAULT]
dhcpbridge_flagfile=/etc/nova/nova.conf
dhcpbridge=/usr/bin/nova-dhcpbridge
logdir=/var/log/nova
state_path=/var/lib/nova
lock_path=/var/lock/nova
force_dhcp_release=True
libvirt_use_virtio_for_bridges=True
verbose=True
ec2_private_dns_show_ip=True
api_paste_config=/etc/nova/api-paste.ini
enabled_apis=ec2,osapi_compute,metadata
rpc_backend = rabbit
auth_strategy = keystone
my_ip = {{ my_ip }}
network_api_class = nova.network.neutronv2.api.API
security_group_api = neutron
linuxnet_interface_driver = nova.network.linux_net.NeutronLinuxBridgeInterfaceDriver
firewall_driver = nova.virt.firewall.NoopFirewallDriver

[oslo_messaging_rabbit]
rabbit_hosts = {{ rabbit_hosts }}
rabbit_userid = openstack
rabbit_password = {{ rabbit_password }}

[keystone_authtoken]
auth_uri = {{ auth_uri }}
auth_url = {{ auth_url }}
auth_plugin = password
project_domain_id = default
user_domain_id = default
project_name = service
username = nova
password = {{ password }}

[vnc]
enabled = True
vncserver_listen = 0.0.0.0
vncserver_proxyclient_address = $my_ip
novncproxy_base_url = {{ novncproxy_base_url }}

[glance]
host = {{ host }}

[oslo_concurrency]
lock_path = /var/lib/nova/tmp

[neutron]
url = {{ url }}
auth_url = {{ auth_url }}
auth_plugin = password
project_domain_id = default
user_domain_id = default
region_name = RegionOne
project_name = service
username = neutron
password = {{ neutron_password }}
"""
conf_nova_compute_conf = """[DEFAULT]
compute_driver=libvirt.LibvirtDriver
[libvirt]
virt_type=kvm
images_type = rbd
images_rbd_pool = vms
images_rbd_ceph_conf = /etc/ceph/ceph.conf
rbd_user = cinder
rbd_secret_uuid = {{ rbd_secret_uuid }}
disk_cachemodes="network=writeback"
live_migration_flag="VIR_MIGRATE_UNDEFINE_SOURCE,VIR_MIGRATE_PEER2PEER,VIR_MIGRATE_LIVE,VIR_MIGRATE_PERSIST_DEST,VIR_MIGRATE_TUNNELLED"
"""
conf_libvirt_bin = """# Defaults for libvirt-bin initscript (/etc/init.d/libvirt-bin)
# This is a POSIX shell fragment

# Start libvirtd to handle qemu/kvm:
start_libvirtd="yes"

# options passed to libvirtd, add "-l" to listen on tcp
libvirtd_opts="-l -d -f /etc/libvirt/libvirtd.conf"

# pass in location of kerberos keytab
#export KRB5_KTNAME=/etc/libvirt/libvirt.keytab
"""
conf_libvirtd_conf = """# Master libvirt daemon configuration file
#
# For further information consult http://libvirt.org/format.html
#
# NOTE: the tests/daemon-conf regression test script requires
# that each "PARAMETER = VALUE" line in this file have the parameter
# name just after a leading "#".

#################################################################
#
# Network connectivity controls
#

# Flag listening for secure TLS connections on the public TCP/IP port.
# NB, must pass the --listen flag to the libvirtd process for this to
# have any effect.
#
# It is necessary to setup a CA and issue server certificates before
# using this capability.
#
# This is enabled by default, uncomment this to disable it
listen_tls = 0

# Listen for unencrypted TCP connections on the public TCP/IP port.
# NB, must pass the --listen flag to the libvirtd process for this to
# have any effect.
#
# Using the TCP socket requires SASL authentication by default. Only
# SASL mechanisms which support data encryption are allowed. This is
# DIGEST_MD5 and GSSAPI (Kerberos5)
#
# This is disabled by default, uncomment this to enable it.
listen_tcp = 1



# Override the port for accepting secure TLS connections
# This can be a port number, or service name
#
#tls_port = "16514"

# Override the port for accepting insecure TCP connections
# This can be a port number, or service name
#
tcp_port = "16509"


# Override the default configuration which binds to all network
# interfaces. This can be a numeric IPv4/6 address, or hostname
#
# If the libvirtd service is started in parallel with network
# startup (e.g. with systemd), binding to addresses other than
# the wildcards (0.0.0.0/::) might not be available yet.
#
#listen_addr = "192.168.0.1"


# Flag toggling mDNS advertizement of the libvirt service.
#
# Alternatively can disable for all services on a host by
# stopping the Avahi daemon
#
# This is disabled by default, uncomment this to enable it
#mdns_adv = 1

# Override the default mDNS advertizement name. This must be
# unique on the immediate broadcast network.
#
# The default is "Virtualization Host HOSTNAME", where HOSTNAME
# is substituted for the short hostname of the machine (without domain)
#
#mdns_name = "Virtualization Host Joe Demo"


#################################################################
#
# UNIX socket access controls
#

# Beware that if you are changing *any* of these options, and you use
# socket activation with systemd, you need to adjust the settings in
# the libvirtd.socket file as well since it could impose a security
# risk if you rely on file permission checking only.

# Set the UNIX domain socket group ownership. This can be used to
# allow a 'trusted' set of users access to management capabilities
# without becoming root.
#
# This is restricted to 'root' by default.
unix_sock_group = "libvirtd"

# Set the UNIX socket permissions for the R/O socket. This is used
# for monitoring VM status only
#
# Default allows any user. If setting group ownership, you may want to
# restrict this too.
unix_sock_ro_perms = "0777"

# Set the UNIX socket permissions for the R/W socket. This is used
# for full management of VMs
#
# Default allows only root. If PolicyKit is enabled on the socket,
# the default will change to allow everyone (eg, 0777)
#
# If not using PolicyKit and setting group ownership for access
# control, then you may want to relax this too.
unix_sock_rw_perms = "0770"

# Set the name of the directory in which sockets will be found/created.
#unix_sock_dir = "/var/run/libvirt"

#################################################################
#
# Authentication.
#
#  - none: do not perform auth checks. If you can connect to the
#          socket you are allowed. This is suitable if there are
#          restrictions on connecting to the socket (eg, UNIX
#          socket permissions), or if there is a lower layer in
#          the network providing auth (eg, TLS/x509 certificates)
#
#  - sasl: use SASL infrastructure. The actual auth scheme is then
#          controlled from /etc/sasl2/libvirt.conf. For the TCP
#          socket only GSSAPI & DIGEST-MD5 mechanisms will be used.
#          For non-TCP or TLS sockets, any scheme is allowed.
#
#  - polkit: use PolicyKit to authenticate. This is only suitable
#            for use on the UNIX sockets. The default policy will
#            require a user to supply their own password to gain
#            full read/write access (aka sudo like), while anyone
#            is allowed read/only access.
#
# Set an authentication scheme for UNIX read-only sockets
# By default socket permissions allow anyone to connect
#
# To restrict monitoring of domains you may wish to enable
# an authentication mechanism here
auth_unix_ro = "none"

# Set an authentication scheme for UNIX read-write sockets
# By default socket permissions only allow root. If PolicyKit
# support was compiled into libvirt, the default will be to
# use 'polkit' auth.
#
# If the unix_sock_rw_perms are changed you may wish to enable
# an authentication mechanism here
auth_unix_rw = "none"

# Change the authentication scheme for TCP sockets.
#
# If you don't enable SASL, then all TCP traffic is cleartext.
# Don't do this outside of a dev/test scenario. For real world
# use, always enable SASL and use the GSSAPI or DIGEST-MD5
# mechanism in /etc/sasl2/libvirt.conf
#auth_tcp = "sasl"
auth_tcp = "none"

# Change the authentication scheme for TLS sockets.
#
# TLS sockets already have encryption provided by the TLS
# layer, and limited authentication is done by certificates
#
# It is possible to make use of any SASL authentication
# mechanism as well, by using 'sasl' for this option
#auth_tls = "none"


# Change the API access control scheme
#
# By default an authenticated user is allowed access
# to all APIs. Access drivers can place restrictions
# on this. By default the 'nop' driver is enabled,
# meaning no access control checks are done once a
# client has authenticated with libvirtd
#
#access_drivers = [ "polkit" ]

#################################################################
#
# TLS x509 certificate configuration
#


# Override the default server key file path
#
#key_file = "/etc/pki/libvirt/private/serverkey.pem"

# Override the default server certificate file path
#
#cert_file = "/etc/pki/libvirt/servercert.pem"

# Override the default CA certificate path
#
#ca_file = "/etc/pki/CA/cacert.pem"

# Specify a certificate revocation list.
#
# Defaults to not using a CRL, uncomment to enable it
#crl_file = "/etc/pki/CA/crl.pem"



#################################################################
#
# Authorization controls
#


# Flag to disable verification of our own server certificates
#
# When libvirtd starts it performs some sanity checks against
# its own certificates.
#
# Default is to always run sanity checks. Uncommenting this
# will disable sanity checks which is not a good idea
#tls_no_sanity_certificate = 1

# Flag to disable verification of client certificates
#
# Client certificate verification is the primary authentication mechanism.
# Any client which does not present a certificate signed by the CA
# will be rejected.
#
# Default is to always verify. Uncommenting this will disable
# verification - make sure an IP whitelist is set
#tls_no_verify_certificate = 1


# A whitelist of allowed x509 Distinguished Names
# This list may contain wildcards such as
#
#    "C=GB,ST=London,L=London,O=Red Hat,CN=*"
#
# See the POSIX fnmatch function for the format of the wildcards.
#
# NB If this is an empty list, no client can connect, so comment out
# entirely rather than using empty list to disable these checks
#
# By default, no DN's are checked
#tls_allowed_dn_list = ["DN1", "DN2"]


# A whitelist of allowed SASL usernames. The format for usernames
# depends on the SASL authentication mechanism. Kerberos usernames
# look like username@REALM
#
# This list may contain wildcards such as
#
#    "*@EXAMPLE.COM"
#
# See the POSIX fnmatch function for the format of the wildcards.
#
# NB If this is an empty list, no client can connect, so comment out
# entirely rather than using empty list to disable these checks
#
# By default, no Username's are checked
#sasl_allowed_username_list = ["joe@EXAMPLE.COM", "fred@EXAMPLE.COM" ]



#################################################################
#
# Processing controls
#

# The maximum number of concurrent client connections to allow
# over all sockets combined.
#max_clients = 5000

# The maximum length of queue of connections waiting to be
# accepted by the daemon. Note, that some protocols supporting
# retransmission may obey this so that a later reattempt at
# connection succeeds.
#max_queued_clients = 1000

# The maximum length of queue of accepted but not yet
# authenticated clients. The default value is zero, meaning
# the feature is disabled.
#max_anonymous_clients = 20

# The minimum limit sets the number of workers to start up
# initially. If the number of active clients exceeds this,
# then more threads are spawned, up to max_workers limit.
# Typically you'd want max_workers to equal maximum number
# of clients allowed
#min_workers = 5
#max_workers = 20


# The number of priority workers. If all workers from above
# pool are stuck, some calls marked as high priority
# (notably domainDestroy) can be executed in this pool.
#prio_workers = 5

# Total global limit on concurrent RPC calls. Should be
# at least as large as max_workers. Beyond this, RPC requests
# will be read into memory and queued. This directly impacts
# memory usage, currently each request requires 256 KB of
# memory. So by default up to 5 MB of memory is used
#
# XXX this isn't actually enforced yet, only the per-client
# limit is used so far
#max_requests = 20

# Limit on concurrent requests from a single client
# connection. To avoid one client monopolizing the server
# this should be a small fraction of the global max_requests
# and max_workers parameter
#max_client_requests = 5

#################################################################
#
# Logging controls
#

# Logging level: 4 errors, 3 warnings, 2 information, 1 debug
# basically 1 will log everything possible
# Note: Journald may employ rate limiting of the messages logged
# and thus lock up the libvirt daemon. To use the debug level with
# journald you have to specify it explicitly in 'log_outputs', otherwise
# only information level messages will be logged.
#log_level = 3

# Logging filters:
# A filter allows to select a different logging level for a given category
# of logs
# The format for a filter is one of:
#    x:name
#    x:+name
#      where name is a string which is matched against source file name,
#      e.g., "remote", "qemu", or "util/json", the optional "+" prefix
#      tells libvirt to log stack trace for each message matching name,
#      and x is the minimal level where matching messages should be logged:
#    1: DEBUG
#    2: INFO
#    3: WARNING
#    4: ERROR
#
# Multiple filters can be defined in a single @filters, they just need to be
# separated by spaces.
#
# e.g. to only get warning or errors from the remote layer and only errors
# from the event layer:
#log_filters="3:remote 4:event"

# Logging outputs:
# An output is one of the places to save logging information
# The format for an output can be:
#    x:stderr
#      output goes to stderr
#    x:syslog:name
#      use syslog for the output and use the given name as the ident
#    x:file:file_path
#      output to a file, with the given filepath
#    x:journald
#      output to journald logging system
# In all case the x prefix is the minimal level, acting as a filter
#    1: DEBUG
#    2: INFO
#    3: WARNING
#    4: ERROR
#
# Multiple outputs can be defined, they just need to be separated by spaces.
# e.g. to log all warnings and errors to syslog under the libvirtd ident:
#log_outputs="3:syslog:libvirtd"
#

# Log debug buffer size:
#
# This configuration option is no longer used, since the global
# log buffer functionality has been removed. Please configure
# suitable log_outputs/log_filters settings to obtain logs.
#log_buffer_size = 64


##################################################################
#
# Auditing
#
# This setting allows usage of the auditing subsystem to be altered:
#
#   audit_level == 0  -> disable all auditing
#   audit_level == 1  -> enable auditing, only if enabled on host (default)
#   audit_level == 2  -> enable auditing, and exit if disabled on host
#
#audit_level = 2
#
# If set to 1, then audit messages will also be sent
# via libvirt logging infrastructure. Defaults to 0
#
#audit_logging = 1

###################################################################
# UUID of the host:
# Provide the UUID of the host here in case the command
# 'dmidecode -s system-uuid' does not provide a valid uuid. In case
# 'dmidecode' does not provide a valid UUID and none is provided here, a
# temporary UUID will be generated.
# Keep the format of the example UUID below. UUID must not have all digits
# be the same.

# NB This default all-zeros UUID will not work. Replace
# it with the output of the 'uuidgen' command and then
# uncomment this entry
#host_uuid = "00000000-0000-0000-0000-000000000000"

###################################################################
# Keepalive protocol:
# This allows libvirtd to detect broken client connections or even
# dead clients.  A keepalive message is sent to a client after
# keepalive_interval seconds of inactivity to check if the client is
# still responding; keepalive_count is a maximum number of keepalive
# messages that are allowed to be sent to the client without getting
# any response before the connection is considered broken.  In other
# words, the connection is automatically closed approximately after
# keepalive_interval * (keepalive_count + 1) seconds since the last
# message received from the client.  If keepalive_interval is set to
# -1, libvirtd will never send keepalive requests; however clients
# can still send them and the daemon will send responses.  When
# keepalive_count is set to 0, connections will be automatically
# closed after keepalive_interval seconds of inactivity without
# sending any keepalive messages.
#
#keepalive_interval = 5
#keepalive_count = 5
#
# If set to 1, libvirtd will refuse to talk to clients that do not
# support keepalive protocol.  Defaults to 0.
#
#keepalive_required = 1
"""

class NovaCompute(Task):
    def __init__(self, user, hosts=None, parallel=True, *args, **kwargs):
        super(NovaCompute, self).__init__(*args, **kwargs)
        self.user = user
        self.hosts = hosts
        self.parallel = parallel
        env.user = self.user
        env.hosts = self.hosts
        env.parallel = self.parallel

    def _install(self, my_ip, rabbit_hosts, rabbit_pass, auth_uri, auth_url, nova_pass, novncproxy_base_url, glance_host, neutron_endpoint, neutron_pass, rbd_secret_uuid):
        print red(env.host_string + ' | Install nova-compute sysfsutils')
        sudo('apt-get update')
        sudo('apt-get -y install nova-compute sysfsutils')

        print red(env.host_string + ' | Update /etc/nova/nova.conf')
        with open('tmp_nova_conf_' + env.host_string, 'w') as f:
            f.write(conf_nova_conf)

        files.upload_template(filename='tmp_nova_conf_'+env.host_string,
                              destination='/etc/nova/nova.conf',
                              use_jinja=True,
                              use_sudo=True,
                              context={'my_ip': my_ip,
                                       'rabbit_hosts': rabbit_hosts,
                                       'rabbit_password': rabbit_pass,
                                       'auth_uri': auth_uri,
                                       'auth_url': auth_url,
                                       'password': nova_pass,
                                       'novncproxy_base_url': novncproxy_base_url,
                                       'host': glance_host,
                                       'url': neutron_endpoint,
                                       'neutron_password': neutron_pass})
        os.remove('tmp_nova_conf_' + env.host_string)

        print red(env.host_string + ' | Update /etc/nova/nova-compute.conf')
        with open('tmp_nova_compute_conf_' + env.host_string, 'w') as f:
            f.write(conf_nova_compute_conf)

        files.upload_template(filename='tmp_nova_compute_conf_'+env.host_string,
                              destination='/etc/nova/nova-compute.conf',
                              use_jinja=True,
                              use_sudo=True,
                              context={'rbd_secret_uuid': rbd_secret_uuid})

        os.remove('tmp_nova_compute_conf_' + env.host_string)

        print red(env.host_string + ' | Restart Compute service')
        sudo('service nova-compute restart')
        print red(env.host_string + ' |  Remove the SQLite database file')
        sudo('rm -f /var/lib/nova/nova.sqlite')

        print red(env.host_string + ' | Enable libvirt listen on 16509')
        print red(env.host_string + ' | Update /etc/default/libvirt-bin')
        with open('tmp_libvirt_bin_' + env.host_string, 'w') as f:
            f.write(conf_libvirt_bin)
        files.upload_template(filename='tmp_libvirt_bin_' + env.host_string,
                              destination='/etc/default/libvirt-bin',
                              use_sudo=True)
        os.remove('tmp_libvirt_bin_' + env.host_string)
        print red(env.host_string + ' | Update /etc/libvirt/libvirtd.conf')
        with open('tmp_libvirtd_conf_' + env.host_string, 'w') as f:
            f.write(conf_libvirtd_conf)
        files.upload_template(filename='tmp_libvirtd_conf_' + env.host_string,
                              destination='/etc/libvirt/libvirtd.conf',
                              use_sudo=True)
        os.remove('tmp_libvirtd_conf_' + env.host_string)
        sudo('restart libvirt-bin')


def main():
    try:
        target = NovaCompute(user=args.user, hosts=args.hosts.split(','))
    except AttributeError:
        print red('No hosts found. Please using --hosts param.')
        parser.print_help()
        sys.exit(1)

    if args.subparser_name == 'install':
        execute(target._install,
                args.my_ip,
                args.rabbit_hosts,
                args.rabbit_pass,
                args.auth_uri,
                args.auth_url,
                args.nova_pass,
                args.novncproxy_base_url,
                args.glance_host,
                args.neutron_endpoint,
                args.neutron_pass,
                args.rbd_secret_uuid)
        

if __name__ == '__main__':
    main()