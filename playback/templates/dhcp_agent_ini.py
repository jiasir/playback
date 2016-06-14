conf_dhcp_agent_ini = """[DEFAULT]
# Show debugging output in log (sets DEBUG log level output)
# debug = False
verbose = True

# The DHCP agent will resync its state with Neutron to recover from any
# transient notification or rpc errors. The interval is number of
# seconds between attempts.
# resync_interval = 5

# The DHCP agent requires an interface driver be set. Choose the one that best
# matches your plugin.
interface_driver = neutron.agent.linux.interface.BridgeInterfaceDriver

# Example of interface_driver option for OVS based plugins(OVS, Ryu, NEC, NVP,
# BigSwitch/Floodlight)
# interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver

# Name of Open vSwitch bridge to use
# ovs_integration_bridge = br-int

# Use veth for an OVS interface or not.
# Support kernels with limited namespace support
# (e.g. RHEL 6.5) so long as ovs_use_veth is set to True.
# ovs_use_veth = False

# Example of interface_driver option for LinuxBridge
# interface_driver = neutron.agent.linux.interface.BridgeInterfaceDriver

# The agent can use other DHCP drivers.  Dnsmasq is the simplest and requires
# no additional setup of the DHCP server.
dhcp_driver = neutron.agent.linux.dhcp.Dnsmasq

# Allow overlapping IP (Must have kernel build with CONFIG_NET_NS=y and
# iproute2 package that supports namespaces). This option is deprecated and
# will be removed in a future release, at which point the old behavior of
# use_namespaces = True will be enforced.
# use_namespaces = True

# In some cases the neutron router is not present to provide the metadata
# IP but the DHCP server can be used to provide this info. Setting this
# value will force the DHCP server to append specific host routes to the
# DHCP request. If this option is set, then the metadata service will be
# activated for all the networks.
# force_metadata = False

# The DHCP server can assist with providing metadata support on isolated
# networks. Setting this value to True will cause the DHCP server to append
# specific host routes to the DHCP request. The metadata service will only
# be activated when the subnet does not contain any router port. The guest
# instance must be configured to request host routes via DHCP (Option 121).
# This option doesn't have any effect when force_metadata is set to True.
enable_isolated_metadata = True

# Allows for serving metadata requests coming from a dedicated metadata
# access network whose cidr is 169.254.169.254/16 (or larger prefix), and
# is connected to a Neutron router from which the VMs send metadata
# request. In this case DHCP Option 121 will not be injected in VMs, as
# they will be able to reach 169.254.169.254 through a router.
# This option requires enable_isolated_metadata = True
# enable_metadata_network = False

# Number of threads to use during sync process. Should not exceed connection
# pool size configured on server.
# num_sync_threads = 4

# Location to store DHCP server config files
# dhcp_confs = $state_path/dhcp

# Domain to use for building the hostnames. This option will be deprecated in
# a future release. It is being replaced by dns_domain in neutron.conf
# dhcp_domain = openstacklocal

# Override the default dnsmasq settings with this file
dnsmasq_config_file = /etc/neutron/dnsmasq-neutron.conf

# Comma-separated list of DNS servers which will be used by dnsmasq
# as forwarders.
# dnsmasq_dns_servers =

# Base log dir for dnsmasq logging. The log contains DHCP and DNS log
# information and is useful for debugging issues with either DHCP or DNS.
# If this section is null, disable dnsmasq log.
# dnsmasq_base_log_dir =

# Limit number of leases to prevent a denial-of-service.
# dnsmasq_lease_max = 16777216

# Location to DHCP lease relay UNIX domain socket
# dhcp_lease_relay_socket = $state_path/dhcp/lease_relay

# Use broadcast in DHCP replies
# dhcp_broadcast_reply = False

# dhcp_delete_namespaces, which is True by default, can be set to False if
# namespaces can't be deleted cleanly on the host running the DHCP agent.
# Disable this if you hit the issue in
# https://bugs.launchpad.net/neutron/+bug/1052535 or if
# you are sure that your version of iproute suffers from the problem.
# This should not be a problem any more.  Refer to bug:
# https://bugs.launchpad.net/neutron/+bug/1418079
# This option is deprecated and will be removed in the M release
# dhcp_delete_namespaces = True

# Timeout for ovs-vsctl commands.
# If the timeout expires, ovs commands will fail with ALARMCLOCK error.
# ovs_vsctl_timeout = 10

[AGENT]
# Log agent heartbeats from this DHCP agent
# log_agent_heartbeats = False
"""
