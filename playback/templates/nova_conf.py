conf_nova_conf = """
[DEFAULT]
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
memcached_servers = {{ memcached_servers }}

[api_database]
connection = {{ api_connection }}

[database]
connection = {{ connection }}

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
vncserver_listen = $my_ip
vncserver_proxyclient_address = $my_ip

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
password = {{ neutron_pass }}

service_metadata_proxy = True
metadata_proxy_shared_secret = {{ metadata_proxy_shared_secret }}


[cinder]
os_region_name = RegionOne
"""
