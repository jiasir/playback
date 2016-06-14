conf_glance_registry_conf = """[DEFAULT]

#
# From glance.registry
#

# When true, this option sets the owner of an image to be the tenant.
# Otherwise, the owner of the  image will be the authenticated user
# issuing the request. (boolean value)
#owner_is_tenant = true

# Role used to identify an authenticated user as administrator.
# (string value)
#admin_role = admin

# Allow unauthenticated users to access the API with read-only
# privileges. This only applies when using ContextMiddleware. (boolean
# value)
#allow_anonymous_access = false

# Limits request ID length. (integer value)
#max_request_id_length = 64

# Whether to allow users to specify image properties beyond what the
# image schema provides (boolean value)
#allow_additional_image_properties = true

# Maximum number of image members per image. Negative values evaluate
# to unlimited. (integer value)
#image_member_quota = 128

# Maximum number of properties allowed on an image. Negative values
# evaluate to unlimited. (integer value)
#image_property_quota = 128

# Maximum number of tags allowed on an image. Negative values evaluate
# to unlimited. (integer value)
#image_tag_quota = 128

# Maximum number of locations allowed on an image. Negative values
# evaluate to unlimited. (integer value)
#image_location_quota = 10

# Python module path of data access API (string value)
#data_api = glance.db.sqlalchemy.api

# Default value for the number of items returned by a request if not
# specified explicitly in the request (integer value)
#limit_param_default = 25

# Maximum permissible number of items that could be returned by a
# request (integer value)
#api_limit_max = 1000

# Whether to include the backend image storage location in image
# properties. Revealing storage location can be a security risk, so
# use this setting with caution! (boolean value)
#show_image_direct_url = false

# Whether to include the backend image locations in image properties.
# For example, if using the file system store a URL of
# "file:///path/to/image" will be returned to the user in the
# 'direct_url' meta-data field. Revealing storage location can be a
# security risk, so use this setting with caution!  The overrides
# show_image_direct_url. (boolean value)
#show_multiple_locations = false

# Maximum size of image a user can upload in bytes. Defaults to
# 1099511627776 bytes (1 TB).WARNING: this value should only be
# increased after careful consideration and must be set to a value
# under 8 EB (9223372036854775808). (integer value)
# Maximum value: 9223372036854775808
#image_size_cap = 1099511627776

# Set a system wide quota for every user. This value is the total
# capacity that a user can use across all storage systems. A value of
# 0 means unlimited.Optional unit can be specified for the value.
# Accepted units are B, KB, MB, GB and TB representing Bytes,
# KiloBytes, MegaBytes, GigaBytes and TeraBytes respectively. If no
# unit is specified then Bytes is assumed. Note that there should not
# be any space between value and unit and units are case sensitive.
# (string value)
#user_storage_quota = 0

# Deploy the v1 OpenStack Images API. (boolean value)
#enable_v1_api = true

# Deploy the v2 OpenStack Images API. (boolean value)
#enable_v2_api = true

# Deploy the v3 OpenStack Objects API. (boolean value)
#enable_v3_api = false

# Deploy the v1 OpenStack Registry API. (boolean value)
#enable_v1_registry = true

# Deploy the v2 OpenStack Registry API. (boolean value)
#enable_v2_registry = true

# The hostname/IP of the pydev process listening for debug connections
# (string value)
#pydev_worker_debug_host = <None>

# The port on which a pydev process is listening for connections.
# (integer value)
# Minimum value: 1
# Maximum value: 65535
#pydev_worker_debug_port = 5678

# AES key for encrypting store 'location' metadata. This includes, if
# used, Swift or S3 credentials. Should be set to a random string of
# length 16, 24 or 32 bytes (string value)
#metadata_encryption_key = <None>

# Digest algorithm which will be used for digital signature. Use the
# command "openssl list-message-digest-algorithms" to get the
# available algorithmssupported by the version of OpenSSL on the
# platform. Examples are "sha1", "sha256", "sha512", etc. (string
# value)
#digest_algorithm = sha256

# Address to bind the server.  Useful when selecting a particular
# network interface. (string value)
#bind_host = 0.0.0.0

# The port on which the server will listen. (integer value)
# Minimum value: 1
# Maximum value: 65535
#bind_port = <None>

# The backlog value that will be used when creating the TCP listener
# socket. (integer value)
#backlog = 4096

# The value for the socket option TCP_KEEPIDLE.  This is the time in
# seconds that the connection must be idle before TCP starts sending
# keepalive probes. (integer value)
#tcp_keepidle = 600

# CA certificate file to use to verify connecting clients. (string
# value)
#ca_file = <None>

# Certificate file to use when starting API server securely. (string
# value)
#cert_file = <None>

# Private key file to use when starting API server securely. (string
# value)
#key_file = <None>

# The number of child process workers that will be created to service
# requests. The default will be equal to the number of CPUs available.
# (integer value)
#workers = 4

# Maximum line size of message headers to be accepted. max_header_line
# may need to be increased when using large tokens (typically those
# generated by the Keystone v3 API with big service catalogs (integer
# value)
#max_header_line = 16384

# If False, server will return the header "Connection: close", If
# True, server will return "Connection: Keep-Alive" in its responses.
# In order to close the client socket connection explicitly after the
# response is sent and read successfully by the client, you simply
# have to set this option to False when you create a wsgi server.
# (boolean value)
#http_keepalive = true

# Timeout for client connections' socket operations. If an incoming
# connection is idle for this number of seconds it will be closed. A
# value of '0' means wait forever. (integer value)
#client_socket_timeout = 900

#
# From oslo.log
#

# Print debugging output (set logging level to DEBUG instead of
# default INFO level). (boolean value)
#debug = false

# If set to false, will disable INFO logging level, making WARNING the
# default. (boolean value)
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
verbose = true

# The name of a logging configuration file. This file is appended to
# any existing logging configuration files. For details about logging
# configuration files, see the Python logging module documentation.
# (string value)
# Deprecated group/name - [DEFAULT]/log_config
#log_config_append = <None>

# DEPRECATED. A logging.Formatter log message format string which may
# use any of the available logging.LogRecord attributes. This option
# is deprecated.  Please use logging_context_format_string and
# logging_default_format_string instead. (string value)
#log_format = <None>

# Format string for %%(asctime)s in log records. Default: %(default)s
# . (string value)
#log_date_format = %Y-%m-%d %H:%M:%S

# (Optional) Name of log file to output to. If no default is set,
# logging will go to stdout. (string value)
# Deprecated group/name - [DEFAULT]/logfile
#log_file = <None>

# (Optional) The base directory used for relative --log-file paths.
# (string value)
# Deprecated group/name - [DEFAULT]/logdir
#log_dir = <None>

# Use syslog for logging. Existing syslog format is DEPRECATED and
# will be changed later to honor RFC5424. (boolean value)
#use_syslog = false

# (Optional) Enables or disables syslog rfc5424 format for logging. If
# enabled, prefixes the MSG part of the syslog message with APP-NAME
# (RFC5424). The format without the APP-NAME is deprecated in Kilo,
# and will be removed in Mitaka, along with this option. (boolean
# value)
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
#use_syslog_rfc_format = true

# Syslog facility to receive log lines. (string value)
#syslog_log_facility = LOG_USER

# Log output to standard error. (boolean value)
#use_stderr = true

# Format string to use for log messages with context. (string value)
#logging_context_format_string = %(asctime)s.%(msecs)03d %(process)d %(levelname)s %(name)s [%(request_id)s %(user_identity)s] %(instance)s%(message)s

# Format string to use for log messages without context. (string
# value)
#logging_default_format_string = %(asctime)s.%(msecs)03d %(process)d %(levelname)s %(name)s [-] %(instance)s%(message)s

# Data to append to log format when level is DEBUG. (string value)
#logging_debug_format_suffix = %(funcName)s %(pathname)s:%(lineno)d

# Prefix each line of exception output with this format. (string
# value)
#logging_exception_prefix = %(asctime)s.%(msecs)03d %(process)d ERROR %(name)s %(instance)s

# List of logger=LEVEL pairs. (list value)
#default_log_levels = amqp=WARN,amqplib=WARN,boto=WARN,qpid=WARN,sqlalchemy=WARN,suds=INFO,oslo.messaging=INFO,iso8601=WARN,requests.packages.urllib3.connectionpool=WARN,urllib3.connectionpool=WARN,websocket=WARN,requests.packages.urllib3.util.retry=WARN,urllib3.util.retry=WARN,keystonemiddleware=WARN,routes.middleware=WARN,stevedore=WARN,taskflow=WARN

# Enables or disables publication of error events. (boolean value)
#publish_errors = false

# The format for an instance that is passed with the log message.
# (string value)
#instance_format = "[instance: %(uuid)s] "

# The format for an instance UUID that is passed with the log message.
# (string value)
#instance_uuid_format = "[instance: %(uuid)s] "

# Enables or disables fatal status of deprecations. (boolean value)
#fatal_deprecations = false

#
# From oslo.messaging
#

# Size of RPC connection pool. (integer value)
# Deprecated group/name - [DEFAULT]/rpc_conn_pool_size
#rpc_conn_pool_size = 30

# ZeroMQ bind address. Should be a wildcard (*), an ethernet
# interface, or IP. The "host" option should point or resolve to this
# address. (string value)
#rpc_zmq_bind_address = *

# MatchMaker driver. (string value)
#rpc_zmq_matchmaker = local

# ZeroMQ receiver listening port. (integer value)
#rpc_zmq_port = 9501

# Number of ZeroMQ contexts, defaults to 1. (integer value)
#rpc_zmq_contexts = 1

# Maximum number of ingress messages to locally buffer per topic.
# Default is unlimited. (integer value)
#rpc_zmq_topic_backlog = <None>

# Directory for holding IPC sockets. (string value)
#rpc_zmq_ipc_dir = /var/run/openstack

# Name of this node. Must be a valid hostname, FQDN, or IP address.
# Must match "host" option, if running Nova. (string value)
#rpc_zmq_host = localhost

# Seconds to wait before a cast expires (TTL). Only supported by
# impl_zmq. (integer value)
#rpc_cast_timeout = 30

# Heartbeat frequency. (integer value)
#matchmaker_heartbeat_freq = 300

# Heartbeat time-to-live. (integer value)
#matchmaker_heartbeat_ttl = 600

# Size of executor thread pool. (integer value)
# Deprecated group/name - [DEFAULT]/rpc_thread_pool_size
#executor_thread_pool_size = 64

# The Drivers(s) to handle sending notifications. Possible values are
# messaging, messagingv2, routing, log, test, noop (multi valued)
notification_driver = noop

# AMQP topic used for OpenStack notifications. (list value)
# Deprecated group/name - [rpc_notifier2]/topics
#notification_topics = notifications

# Seconds to wait for a response from a call. (integer value)
#rpc_response_timeout = 60

# A URL representing the messaging driver to use and its full
# configuration. If not set, we fall back to the rpc_backend option
# and driver specific configuration. (string value)
#transport_url = <None>

# The messaging driver to use, defaults to rabbit. Other drivers
# include qpid and zmq. (string value)
#rpc_backend = rabbit

# The default exchange under which topics are scoped. May be
# overridden by an exchange name specified in the transport_url
# option. (string value)
#control_exchange = openstack


[database]

#
# From oslo.db
#

# The file name to use with SQLite. (string value)
# Deprecated group/name - [DEFAULT]/sqlite_db
#sqlite_db = oslo.sqlite
sqlite_db = /var/lib/glance/glance.sqlite

# If True, SQLite uses synchronous mode. (boolean value)
# Deprecated group/name - [DEFAULT]/sqlite_synchronous
#sqlite_synchronous = true

# The back end to use for the database. (string value)
# Deprecated group/name - [DEFAULT]/db_backend
backend = sqlalchemy

# The SQLAlchemy connection string to use to connect to the database.
# (string value)
# Deprecated group/name - [DEFAULT]/sql_connection
# Deprecated group/name - [DATABASE]/sql_connection
# Deprecated group/name - [sql]/connection
connection = {{ connection }}

# The SQLAlchemy connection string to use to connect to the slave
# database. (string value)
#slave_connection = <None>

# The SQL mode to be used for MySQL sessions. This option, including
# the default, overrides any server-set SQL mode. To use whatever SQL
# mode is set by the server configuration, set this to no value.
# Example: mysql_sql_mode= (string value)
#mysql_sql_mode = TRADITIONAL

# Timeout before idle SQL connections are reaped. (integer value)
# Deprecated group/name - [DEFAULT]/sql_idle_timeout
# Deprecated group/name - [DATABASE]/sql_idle_timeout
# Deprecated group/name - [sql]/idle_timeout
#idle_timeout = 3600

# Minimum number of SQL connections to keep open in a pool. (integer
# value)
# Deprecated group/name - [DEFAULT]/sql_min_pool_size
# Deprecated group/name - [DATABASE]/sql_min_pool_size
#min_pool_size = 1

# Maximum number of SQL connections to keep open in a pool. (integer
# value)
# Deprecated group/name - [DEFAULT]/sql_max_pool_size
# Deprecated group/name - [DATABASE]/sql_max_pool_size
#max_pool_size = <None>

# Maximum number of database connection retries during startup. Set to
# -1 to specify an infinite retry count. (integer value)
# Deprecated group/name - [DEFAULT]/sql_max_retries
# Deprecated group/name - [DATABASE]/sql_max_retries
#max_retries = 10

# Interval between retries of opening a SQL connection. (integer
# value)
# Deprecated group/name - [DEFAULT]/sql_retry_interval
# Deprecated group/name - [DATABASE]/reconnect_interval
#retry_interval = 10

# If set, use this value for max_overflow with SQLAlchemy. (integer
# value)
# Deprecated group/name - [DEFAULT]/sql_max_overflow
# Deprecated group/name - [DATABASE]/sqlalchemy_max_overflow
#max_overflow = <None>

# Verbosity of SQL debugging information: 0=None, 100=Everything.
# (integer value)
# Deprecated group/name - [DEFAULT]/sql_connection_debug
#connection_debug = 0

# Add Python stack traces to SQL as comment strings. (boolean value)
# Deprecated group/name - [DEFAULT]/sql_connection_trace
#connection_trace = false

# If set, use this value for pool_timeout with SQLAlchemy. (integer
# value)
# Deprecated group/name - [DATABASE]/sqlalchemy_pool_timeout
#pool_timeout = <None>

# Enable the experimental use of database reconnect on connection
# lost. (boolean value)
#use_db_reconnect = false

# Seconds between retries of a database transaction. (integer value)
#db_retry_interval = 1

# If True, increases the interval between retries of a database
# operation up to db_max_retry_interval. (boolean value)
#db_inc_retry_interval = true

# If db_inc_retry_interval is set, the maximum seconds between retries
# of a database operation. (integer value)
#db_max_retry_interval = 10

# Maximum retries in case of connection error or deadlock error before
# error is raised. Set to -1 to specify an infinite retry count.
# (integer value)
#db_max_retries = 20

#
# From oslo.db.concurrency
#

# Enable the experimental use of thread pooling for all DB API calls
# (boolean value)
# Deprecated group/name - [DEFAULT]/dbapi_use_tpool
#use_tpool = false


[glance_store]

#
# From glance.store
#

# List of stores enabled (list value)
#stores = file,http

# Default scheme to use to store image data. The scheme must be
# registered by one of the stores defined by the 'stores' config
# option. (string value)
#default_store = file

# Minimum interval seconds to execute updating dynamic storage
# capabilities based on backend status then. It's not a periodic
# routine, the update logic will be executed only when interval
# seconds elapsed and an operation of store has triggered. The feature
# will be enabled only when the option value greater then zero.
# (integer value)
#store_capabilities_update_min_interval = 0

#
# From glance.store
#

# If True, swiftclient won't check for a valid SSL certificate when
# authenticating. (boolean value)
#swift_store_auth_insecure = false

# A string giving the CA certificate file to use in SSL connections
# for verifying certs. (string value)
#swift_store_cacert = <None>

# The region of the swift endpoint to be used for single tenant. This
# setting is only necessary if the tenant has multiple swift
# endpoints. (string value)
#swift_store_region = <None>

# If set, the configured endpoint will be used. If None, the storage
# url from the auth response will be used. (string value)
#swift_store_endpoint = <None>

# A string giving the endpoint type of the swift service to use
# (publicURL, adminURL or internalURL). This setting is only used if
# swift_store_auth_version is 2. (string value)
#swift_store_endpoint_type = publicURL

# A string giving the service type of the swift service to use. This
# setting is only used if swift_store_auth_version is 2. (string
# value)
#swift_store_service_type = object-store

# Container within the account that the account should use for storing
# images in Swift when using single container mode. In multiple
# container mode, this will be the prefix for all containers. (string
# value)
#swift_store_container = glance

# The size, in MB, that Glance will start chunking image files and do
# a large object manifest in Swift. (integer value)
#swift_store_large_object_size = 5120

# The amount of data written to a temporary disk buffer during the
# process of chunking the image file. (integer value)
#swift_store_large_object_chunk_size = 200

# A boolean value that determines if we create the container if it
# does not exist. (boolean value)
#swift_store_create_container_on_put = false

# If set to True, enables multi-tenant storage mode which causes
# Glance images to be stored in tenant specific Swift accounts.
# (boolean value)
#swift_store_multi_tenant = false

# When set to 0, a single-tenant store will only use one container to
# store all images. When set to an integer value between 1 and 32, a
# single-tenant store will use multiple containers to store images,
# and this value will determine how many containers are created.Used
# only when swift_store_multi_tenant is disabled. The total number of
# containers that will be used is equal to 16^N, so if this config
# option is set to 2, then 16^2=256 containers will be used to store
# images. (integer value)
#swift_store_multiple_containers_seed = 0

# A list of tenants that will be granted read/write access on all
# Swift containers created by Glance in multi-tenant mode. (list
# value)
#swift_store_admin_tenants =

# If set to False, disables SSL layer compression of https swift
# requests. Setting to False may improve performance for images which
# are already in a compressed format, eg qcow2. (boolean value)
#swift_store_ssl_compression = true

# The number of times a Swift download will be retried before the
# request fails. (integer value)
#swift_store_retry_get_count = 0

# The reference to the default swift account/backing store parameters
# to use for adding new images. (string value)
#default_swift_reference = ref1

# Version of the authentication service to use. Valid versions are 2
# and 3 for keystone and 1 (deprecated) for swauth and rackspace.
# (deprecated - use "auth_version" in swift_store_config_file) (string
# value)
#swift_store_auth_version = 2

# The address where the Swift authentication service is listening.
# (deprecated - use "auth_address" in swift_store_config_file) (string
# value)
#swift_store_auth_address = <None>

# The user to authenticate against the Swift authentication service
# (deprecated - use "user" in swift_store_config_file) (string value)
#swift_store_user = <None>

# Auth key for the user authenticating against the Swift
# authentication service. (deprecated - use "key" in
# swift_store_config_file) (string value)
#swift_store_key = <None>

# The config file that has the swift account(s)configs. (string value)
#swift_store_config_file = <None>

# The host where the S3 server is listening. (string value)
#s3_store_host = <None>

# The S3 query token access key. (string value)
#s3_store_access_key = <None>

# The S3 query token secret key. (string value)
#s3_store_secret_key = <None>

# The S3 bucket to be used to store the Glance data. (string value)
#s3_store_bucket = <None>

# The local directory where uploads will be staged before they are
# transferred into S3. (string value)
#s3_store_object_buffer_dir = <None>

# A boolean to determine if the S3 bucket should be created on upload
# if it does not exist or if an error should be returned to the user.
# (boolean value)
#s3_store_create_bucket_on_put = false

# The S3 calling format used to determine the bucket. Either subdomain
# or path can be used. (string value)
#s3_store_bucket_url_format = subdomain

# What size, in MB, should S3 start chunking image files and do a
# multipart upload in S3. (integer value)
#s3_store_large_object_size = 100

# What multipart upload part size, in MB, should S3 use when uploading
# parts. The size must be greater than or equal to 5M. (integer value)
#s3_store_large_object_chunk_size = 10

# The number of thread pools to perform a multipart upload in S3.
# (integer value)
#s3_store_thread_pools = 10

# Directory to which the Filesystem backend store writes images.
# (string value)
#filesystem_store_datadir = <None>

# List of directories and its priorities to which the Filesystem
# backend store writes images. (multi valued)
#filesystem_store_datadirs =

# The path to a file which contains the metadata to be returned with
# any location associated with this store.  The file must contain a
# valid JSON object. The object should contain the keys 'id' and
# 'mountpoint'. The value for both keys should be 'string'. (string
# value)
#filesystem_store_metadata_file = <None>

# The required permission for created image file. In this way the user
# other service used, e.g. Nova, who consumes the image could be the
# exclusive member of the group that owns the files created. Assigning
# it less then or equal to zero means don't change the default
# permission of the file. This value will be decoded as an octal
# digit. (integer value)
#filesystem_store_file_perm = 0

# ESX/ESXi or vCenter Server target system. The server value can be an
# IP address or a DNS name. (string value)
#vmware_server_host = <None>

# Username for authenticating with VMware ESX/VC server. (string
# value)
#vmware_server_username = <None>

# Password for authenticating with VMware ESX/VC server. (string
# value)
#vmware_server_password = <None>

# DEPRECATED. Inventory path to a datacenter. If the
# vmware_server_host specified is an ESX/ESXi, the
# vmware_datacenter_path is optional. If specified, it should be "ha-
# datacenter". This option is deprecated in favor of vmware_datastores
# and will be removed in the Liberty release. (string value)
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
#vmware_datacenter_path = ha-datacenter

# DEPRECATED. Datastore associated with the datacenter. This option is
# deprecated in favor of vmware_datastores and will be removed in the
# Liberty release. (string value)
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
#vmware_datastore_name = <None>

# Number of times VMware ESX/VC server API must be retried upon
# connection related issues. (integer value)
#vmware_api_retry_count = 10

# The interval used for polling remote tasks invoked on VMware ESX/VC
# server. (integer value)
#vmware_task_poll_interval = 5

# The name of the directory where the glance images will be stored in
# the VMware datastore. (string value)
#vmware_store_image_dir = /openstack_glance

# Allow to perform insecure SSL requests to ESX/VC. (boolean value)
#vmware_api_insecure = false

# A list of datastores where the image can be stored. This option may
# be specified multiple times for specifying multiple datastores.
# Either one of vmware_datastore_name or vmware_datastores is
# required. The datastore name should be specified after its
# datacenter path, seperated by ":". An optional weight may be given
# after the datastore name, seperated again by ":". Thus, the required
# format becomes <datacenter_path>:<datastore_name>:<optional_weight>.
# When adding an image, the datastore with highest weight will be
# selected, unless there is not enough free space available in cases
# where the image size is already known. If no weight is given, it is
# assumed to be zero and the directory will be considered for
# selection last. If multiple datastores have the same weight, then
# the one with the most free space available is selected. (multi
# valued)
#vmware_datastores =

# Images will be chunked into objects of this size (in megabytes). For
# best performance, this should be a power of two. (integer value)
#sheepdog_store_chunk_size = 64

# Port of sheep daemon. (integer value)
#sheepdog_store_port = 7000

# IP address of sheep daemon. (string value)
#sheepdog_store_address = localhost

# RADOS images will be chunked into objects of this size (in
# megabytes). For best performance, this should be a power of two.
# (integer value)
#rbd_store_chunk_size = 8

# RADOS pool in which images are stored. (string value)
#rbd_store_pool = images

# RADOS user to authenticate as (only applicable if using Cephx. If
# <None>, a default will be chosen based on the client. section in
# rbd_store_ceph_conf) (string value)
#rbd_store_user = <None>

# Ceph configuration file path. If <None>, librados will locate the
# default config. If using cephx authentication, this file should
# include a reference to the right keyring in a client.<USER> section
# (string value)
#rbd_store_ceph_conf = /etc/ceph/ceph.conf

# Info to match when looking for cinder in the service catalog. Format
# is : separated values of the form:
# <service_type>:<service_name>:<endpoint_type> (string value)
#cinder_catalog_info = volume:cinder:publicURL

# Override service catalog lookup with template for cinder endpoint
# e.g. http://localhost:8776/v1/%(project_id)s (string value)
#cinder_endpoint_template = <None>

# Region name of this node (string value)
#os_region_name = <None>

# Location of ca certicates file to use for cinder client requests.
# (string value)
#cinder_ca_certificates_file = <None>

# Number of cinderclient retries on failed http calls (integer value)
#cinder_http_retries = 3

# Allow to perform insecure SSL requests to cinder (boolean value)
#cinder_api_insecure = false

# Hostname or IP address of the instance to connect to, or a mongodb
# URI, or a list of hostnames / mongodb URIs. If host is an IPv6
# literal it must be enclosed in '[' and ']' characters following the
# RFC2732 URL syntax (e.g. '[::1]' for localhost) (string value)
#mongodb_store_uri = <None>

# Database to use (string value)
#mongodb_store_db = <None>


[keystone_authtoken]

#
# From keystonemiddleware.auth_token
#

# Complete public Identity API endpoint. (string value)
auth_uri = {{ auth_uri }}
auth_url = {{ auth_url }}
memcached_servers = {{ memcached_servers }}
auth_type = password
project_domain_name = default
user_domain_name = default
project_name = service
username = glance
password = {{ password }}


# API version of the admin Identity API endpoint. (string value)
#auth_version = <None>

# Do not handle authorization requests within the middleware, but
# delegate the authorization decision to downstream WSGI components.
# (boolean value)
#delay_auth_decision = false

# Request timeout value for communicating with Identity API server.
# (integer value)
#http_connect_timeout = <None>

# How many times are we trying to reconnect when communicating with
# Identity API Server. (integer value)
#http_request_max_retries = 3

# Env key for the swift cache. (string value)
#cache = <None>

# Required if identity server requires client certificate (string
# value)
#certfile = <None>

# Required if identity server requires client certificate (string
# value)
#keyfile = <None>

# A PEM encoded Certificate Authority to use when verifying HTTPs
# connections. Defaults to system CAs. (string value)
#cafile = <None>

# Verify HTTPS connections. (boolean value)
#insecure = false

# The region in which the identity server can be found. (string value)
#region_name = <None>

# Directory used to cache files related to PKI tokens. (string value)
#signing_dir = <None>

# Optionally specify a list of memcached server(s) to use for caching.
# If left undefined, tokens will instead be cached in-process. (list
# value)
# Deprecated group/name - [DEFAULT]/memcache_servers
#memcached_servers = <None>

# In order to prevent excessive effort spent validating tokens, the
# middleware caches previously-seen tokens for a configurable duration
# (in seconds). Set to -1 to disable caching completely. (integer
# value)
#token_cache_time = 300

# Determines the frequency at which the list of revoked tokens is
# retrieved from the Identity service (in seconds). A high number of
# revocation events combined with a low cache duration may
# significantly reduce performance. (integer value)
#revocation_cache_time = 10

# (Optional) If defined, indicate whether token data should be
# authenticated or authenticated and encrypted. Acceptable values are
# MAC or ENCRYPT.  If MAC, token data is authenticated (with HMAC) in
# the cache. If ENCRYPT, token data is encrypted and authenticated in
# the cache. If the value is not one of these options or empty,
# auth_token will raise an exception on initialization. (string value)
#memcache_security_strategy = <None>

# (Optional, mandatory if memcache_security_strategy is defined) This
# string is used for key derivation. (string value)
#memcache_secret_key = <None>

# (Optional) Number of seconds memcached server is considered dead
# before it is tried again. (integer value)
#memcache_pool_dead_retry = 300

# (Optional) Maximum total number of open connections to every
# memcached server. (integer value)
#memcache_pool_maxsize = 10

# (Optional) Socket timeout in seconds for communicating with a
# memcached server. (integer value)
#memcache_pool_socket_timeout = 3

# (Optional) Number of seconds a connection to memcached is held
# unused in the pool before it is closed. (integer value)
#memcache_pool_unused_timeout = 60

# (Optional) Number of seconds that an operation will wait to get a
# memcached client connection from the pool. (integer value)
#memcache_pool_conn_get_timeout = 10

# (Optional) Use the advanced (eventlet safe) memcached client pool.
# The advanced pool will only work under python 2.x. (boolean value)
#memcache_use_advanced_pool = false

# (Optional) Indicate whether to set the X-Service-Catalog header. If
# False, middleware will not ask for service catalog on token
# validation and will not set the X-Service-Catalog header. (boolean
# value)
#include_service_catalog = true

# Used to control the use and type of token binding. Can be set to:
# "disabled" to not check token binding. "permissive" (default) to
# validate binding information if the bind type is of a form known to
# the server and ignore it if not. "strict" like "permissive" but if
# the bind type is unknown the token will be rejected. "required" any
# form of token binding is needed to be allowed. Finally the name of a
# binding method that must be present in tokens. (string value)
#enforce_token_bind = permissive

# If true, the revocation list will be checked for cached tokens. This
# requires that PKI tokens are configured on the identity server.
# (boolean value)
#check_revocations_for_cached = false

# Hash algorithms to use for hashing PKI tokens. This may be a single
# algorithm or multiple. The algorithms are those supported by Python
# standard hashlib.new(). The hashes will be tried in the order given,
# so put the preferred one first for performance. The result of the
# first hash will be stored in the cache. This will typically be set
# to multiple values only while migrating from a less secure algorithm
# to a more secure one. Once all the old tokens are expired this
# option should be set to a single value for better performance. (list
# value)
#hash_algorithms = md5

# Prefix to prepend at the beginning of the path. Deprecated, use
# identity_uri. (string value)
#auth_admin_prefix =

# Host providing the admin Identity API endpoint. Deprecated, use
# identity_uri. (string value)
#auth_host = 127.0.0.1

# Port of the admin Identity API endpoint. Deprecated, use
# identity_uri. (integer value)
#auth_port = 35357

# Protocol of the admin Identity API endpoint (http or https).
# Deprecated, use identity_uri. (string value)
#auth_protocol = https

# Complete admin Identity API endpoint. This should specify the
# unversioned root endpoint e.g. https://localhost:35357/ (string
# value)
#identity_uri = <None>

# This option is deprecated and may be removed in a future release.
# Single shared secret with the Keystone configuration used for
# bootstrapping a Keystone installation, or otherwise bypassing the
# normal authentication process. This option should not be used, use
# `admin_user` and `admin_password` instead. (string value)
#admin_token = <None>

# Service username. (string value)
#admin_user = <None>

# Service user password. (string value)
#admin_password = <None>

# Service tenant name. (string value)
#admin_tenant_name = admin


[matchmaker_redis]

#
# From oslo.messaging
#

# Host to locate redis. (string value)
#host = 127.0.0.1

# Use this port to connect to redis host. (integer value)
#port = 6379

# Password for Redis server (optional). (string value)
#password = <None>


[matchmaker_ring]

#
# From oslo.messaging
#

# Matchmaker ring file (JSON). (string value)
# Deprecated group/name - [DEFAULT]/matchmaker_ringfile
#ringfile = /etc/oslo/matchmaker_ring.json


[oslo_messaging_amqp]

#
# From oslo.messaging
#

# address prefix used when sending to a specific server (string value)
# Deprecated group/name - [amqp1]/server_request_prefix
#server_request_prefix = exclusive

# address prefix used when broadcasting to all servers (string value)
# Deprecated group/name - [amqp1]/broadcast_prefix
#broadcast_prefix = broadcast

# address prefix when sending to any server in group (string value)
# Deprecated group/name - [amqp1]/group_request_prefix
#group_request_prefix = unicast

# Name for the AMQP container (string value)
# Deprecated group/name - [amqp1]/container_name
#container_name = <None>

# Timeout for inactive connections (in seconds) (integer value)
# Deprecated group/name - [amqp1]/idle_timeout
#idle_timeout = 0

# Debug: dump AMQP frames to stdout (boolean value)
# Deprecated group/name - [amqp1]/trace
#trace = false

# CA certificate PEM file to verify server certificate (string value)
# Deprecated group/name - [amqp1]/ssl_ca_file
#ssl_ca_file =

# Identifying certificate PEM file to present to clients (string
# value)
# Deprecated group/name - [amqp1]/ssl_cert_file
#ssl_cert_file =

# Private key PEM file used to sign cert_file certificate (string
# value)
# Deprecated group/name - [amqp1]/ssl_key_file
#ssl_key_file =

# Password for decrypting ssl_key_file (if encrypted) (string value)
# Deprecated group/name - [amqp1]/ssl_key_password
#ssl_key_password = <None>

# Accept clients using either SSL or plain TCP (boolean value)
# Deprecated group/name - [amqp1]/allow_insecure_clients
#allow_insecure_clients = false


[oslo_messaging_qpid]

#
# From oslo.messaging
#

# Use durable queues in AMQP. (boolean value)
# Deprecated group/name - [DEFAULT]/amqp_durable_queues
# Deprecated group/name - [DEFAULT]/rabbit_durable_queues
#amqp_durable_queues = false

# Auto-delete queues in AMQP. (boolean value)
# Deprecated group/name - [DEFAULT]/amqp_auto_delete
#amqp_auto_delete = false

# Send a single AMQP reply to call message. The current behaviour
# since oslo-incubator is to send two AMQP replies - first one with
# the payload, a second one to ensure the other have finish to send
# the payload. We are going to remove it in the N release, but we must
# keep backward compatible at the same time. This option provides such
# compatibility - it defaults to False in Liberty and can be turned on
# for early adopters with a new installations or for testing. Please
# note, that this option will be removed in the Mitaka release.
# (boolean value)
#send_single_reply = false

# Qpid broker hostname. (string value)
# Deprecated group/name - [DEFAULT]/qpid_hostname
#qpid_hostname = localhost

# Qpid broker port. (integer value)
# Deprecated group/name - [DEFAULT]/qpid_port
#qpid_port = 5672

# Qpid HA cluster host:port pairs. (list value)
# Deprecated group/name - [DEFAULT]/qpid_hosts
#qpid_hosts = $qpid_hostname:$qpid_port

# Username for Qpid connection. (string value)
# Deprecated group/name - [DEFAULT]/qpid_username
#qpid_username =

# Password for Qpid connection. (string value)
# Deprecated group/name - [DEFAULT]/qpid_password
#qpid_password =

# Space separated list of SASL mechanisms to use for auth. (string
# value)
# Deprecated group/name - [DEFAULT]/qpid_sasl_mechanisms
#qpid_sasl_mechanisms =

# Seconds between connection keepalive heartbeats. (integer value)
# Deprecated group/name - [DEFAULT]/qpid_heartbeat
#qpid_heartbeat = 60

# Transport to use, either 'tcp' or 'ssl'. (string value)
# Deprecated group/name - [DEFAULT]/qpid_protocol
#qpid_protocol = tcp

# Whether to disable the Nagle algorithm. (boolean value)
# Deprecated group/name - [DEFAULT]/qpid_tcp_nodelay
#qpid_tcp_nodelay = true

# The number of prefetched messages held by receiver. (integer value)
# Deprecated group/name - [DEFAULT]/qpid_receiver_capacity
#qpid_receiver_capacity = 1

# The qpid topology version to use.  Version 1 is what was originally
# used by impl_qpid.  Version 2 includes some backwards-incompatible
# changes that allow broker federation to work.  Users should update
# to version 2 when they are able to take everything down, as it
# requires a clean break. (integer value)
# Deprecated group/name - [DEFAULT]/qpid_topology_version
#qpid_topology_version = 1


[oslo_messaging_rabbit]

#
# From oslo.messaging
#

# Use durable queues in AMQP. (boolean value)
# Deprecated group/name - [DEFAULT]/amqp_durable_queues
# Deprecated group/name - [DEFAULT]/rabbit_durable_queues
#amqp_durable_queues = false

# Auto-delete queues in AMQP. (boolean value)
# Deprecated group/name - [DEFAULT]/amqp_auto_delete
#amqp_auto_delete = false

# Send a single AMQP reply to call message. The current behaviour
# since oslo-incubator is to send two AMQP replies - first one with
# the payload, a second one to ensure the other have finish to send
# the payload. We are going to remove it in the N release, but we must
# keep backward compatible at the same time. This option provides such
# compatibility - it defaults to False in Liberty and can be turned on
# for early adopters with a new installations or for testing. Please
# note, that this option will be removed in the Mitaka release.
# (boolean value)
#send_single_reply = false

# SSL version to use (valid only if SSL enabled). Valid values are
# TLSv1 and SSLv23. SSLv2, SSLv3, TLSv1_1, and TLSv1_2 may be
# available on some distributions. (string value)
# Deprecated group/name - [DEFAULT]/kombu_ssl_version
#kombu_ssl_version =

# SSL key file (valid only if SSL enabled). (string value)
# Deprecated group/name - [DEFAULT]/kombu_ssl_keyfile
#kombu_ssl_keyfile =

# SSL cert file (valid only if SSL enabled). (string value)
# Deprecated group/name - [DEFAULT]/kombu_ssl_certfile
#kombu_ssl_certfile =

# SSL certification authority file (valid only if SSL enabled).
# (string value)
# Deprecated group/name - [DEFAULT]/kombu_ssl_ca_certs
#kombu_ssl_ca_certs =

# How long to wait before reconnecting in response to an AMQP consumer
# cancel notification. (floating point value)
# Deprecated group/name - [DEFAULT]/kombu_reconnect_delay
#kombu_reconnect_delay = 1.0

# How long to wait before considering a reconnect attempt to have
# failed. This value should not be longer than rpc_response_timeout.
# (integer value)
#kombu_reconnect_timeout = 60

# The RabbitMQ broker address where a single node is used. (string
# value)
# Deprecated group/name - [DEFAULT]/rabbit_host
#rabbit_host = localhost

# The RabbitMQ broker port where a single node is used. (integer
# value)
# Deprecated group/name - [DEFAULT]/rabbit_port
#rabbit_port = 5672

# RabbitMQ HA cluster host:port pairs. (list value)
# Deprecated group/name - [DEFAULT]/rabbit_hosts
#rabbit_hosts = $rabbit_host:$rabbit_port

# Connect over SSL for RabbitMQ. (boolean value)
# Deprecated group/name - [DEFAULT]/rabbit_use_ssl
#rabbit_use_ssl = false

# The RabbitMQ userid. (string value)
# Deprecated group/name - [DEFAULT]/rabbit_userid
#rabbit_userid = guest

# The RabbitMQ password. (string value)
# Deprecated group/name - [DEFAULT]/rabbit_password
#rabbit_password = guest

# The RabbitMQ login method. (string value)
# Deprecated group/name - [DEFAULT]/rabbit_login_method
#rabbit_login_method = AMQPLAIN

# The RabbitMQ virtual host. (string value)
# Deprecated group/name - [DEFAULT]/rabbit_virtual_host
#rabbit_virtual_host = /

# How frequently to retry connecting with RabbitMQ. (integer value)
#rabbit_retry_interval = 1

# How long to backoff for between retries when connecting to RabbitMQ.
# (integer value)
# Deprecated group/name - [DEFAULT]/rabbit_retry_backoff
#rabbit_retry_backoff = 2

# Maximum number of RabbitMQ connection retries. Default is 0
# (infinite retry count). (integer value)
# Deprecated group/name - [DEFAULT]/rabbit_max_retries
#rabbit_max_retries = 0

# Use HA queues in RabbitMQ (x-ha-policy: all). If you change this
# option, you must wipe the RabbitMQ database. (boolean value)
# Deprecated group/name - [DEFAULT]/rabbit_ha_queues
#rabbit_ha_queues = false

# Number of seconds after which the Rabbit broker is considered down
# if heartbeat's keep-alive fails (0 disable the heartbeat).
# EXPERIMENTAL (integer value)
#heartbeat_timeout_threshold = 60

# How often times during the heartbeat_timeout_threshold we check the
# heartbeat. (integer value)
#heartbeat_rate = 2

# Deprecated, use rpc_backend=kombu+memory or rpc_backend=fake
# (boolean value)
# Deprecated group/name - [DEFAULT]/fake_rabbit
#fake_rabbit = false


[oslo_policy]

#
# From oslo.policy
#

# The JSON file that defines policies. (string value)
# Deprecated group/name - [DEFAULT]/policy_file
#policy_file = policy.json

# Default rule. Enforced when a requested rule is not found. (string
# value)
# Deprecated group/name - [DEFAULT]/policy_default_rule
#policy_default_rule = default

# Directories where policy configuration files are stored. They can be
# relative to any directory in the search path defined by the
# config_dir option, or absolute paths. The file defined by
# policy_file must exist for these directories to be searched.
# Missing or empty directories are ignored. (multi valued)
# Deprecated group/name - [DEFAULT]/policy_dirs
# This option is deprecated for removal.
# Its value may be silently ignored in the future.
#policy_dirs = policy.d


[paste_deploy]

#
# From glance.registry
#

# Partial name of a pipeline in your paste configuration file with the
# service name removed. For example, if your paste section name is
# [pipeline:glance-api-keystone] use the value "keystone" (string
# value)
flavor = keystone

# Name of the paste configuration file. (string value)
#config_file = <None>
"""
