conf_manila_conf = """[DEFAULT]
default_share_type = default_share_type
rootwrap_config = /etc/manila/rootwrap.conf
auth_strategy = keystone
my_ip = {{ my_ip }}
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
# Allowed values: redis, dummy
#rpc_zmq_matchmaker = redis

# Type of concurrency used. Either "native" or "eventlet" (string
# value)
#rpc_zmq_concurrency = eventlet

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

# Seconds to wait before a cast expires (TTL). The default value of -1
# specifies an infinite linger period. The value of 0 specifies no
# linger period. Pending messages shall be discarded immediately when
# the socket is closed. Only supported by impl_zmq. (integer value)
#rpc_cast_timeout = -1

# The default number of seconds that poll should wait. Poll raises
# timeout exception when timeout expired. (integer value)
#rpc_poll_timeout = 1

# Expiration timeout in seconds of a name service record about
# existing target ( < 0 means no timeout). (integer value)
#zmq_target_expire = 120

# Use PUB/SUB pattern for fanout methods. PUB/SUB always uses proxy.
# (boolean value)
#use_pub_sub = true

# Minimal port number for random ports range. (port value)
# Minimum value: 0
# Maximum value: 65535
#rpc_zmq_min_port = 49152

# Maximal port number for random ports range. (integer value)
# Minimum value: 1
# Maximum value: 65536
#rpc_zmq_max_port = 65536

# Number of retries to find free port number before fail with
# ZMQBindError. (integer value)
#rpc_zmq_bind_port_retries = 100

# Size of executor thread pool. (integer value)
# Deprecated group/name - [DEFAULT]/rpc_thread_pool_size
#executor_thread_pool_size = 64

# Seconds to wait for a response from a call. (integer value)
#rpc_response_timeout = 60

# A URL representing the messaging driver to use and its full
# configuration. If not set, we fall back to the rpc_backend option
# and driver specific configuration. (string value)
#transport_url = <None>

# The messaging driver to use, defaults to rabbit. Other drivers
# include amqp and zmq. (string value)
rpc_backend = rabbit

# The default exchange under which topics are scoped. May be
# overridden by an exchange name specified in the transport_url
# option. (string value)
#control_exchange = openstack


[cors]

#
# From oslo.middleware.cors
#

# Indicate whether this resource may be shared with the domain
# received in the requests "origin" header. (list value)
#allowed_origin = <None>

# Indicate that the actual request can include user credentials
# (boolean value)
#allow_credentials = true

# Indicate which headers are safe to expose to the API. Defaults to
# HTTP Simple Headers. (list value)
#expose_headers = Content-Type,Cache-Control,Content-Language,Expires,Last-Modified,Pragma

# Maximum cache age of CORS preflight requests. (integer value)
#max_age = 3600

# Indicate which methods can be used during the actual request. (list
# value)
#allow_methods = GET,POST,PUT,DELETE,OPTIONS

# Indicate which header field names may be used during the actual
# request. (list value)
#allow_headers = Content-Type,Cache-Control,Content-Language,Expires,Last-Modified,Pragma


[cors.subdomain]

#
# From oslo.middleware.cors
#

# Indicate whether this resource may be shared with the domain
# received in the requests "origin" header. (list value)
#allowed_origin = <None>

# Indicate that the actual request can include user credentials
# (boolean value)
#allow_credentials = true

# Indicate which headers are safe to expose to the API. Defaults to
# HTTP Simple Headers. (list value)
#expose_headers = Content-Type,Cache-Control,Content-Language,Expires,Last-Modified,Pragma

# Maximum cache age of CORS preflight requests. (integer value)
#max_age = 3600

# Indicate which methods can be used during the actual request. (list
# value)
#allow_methods = GET,POST,PUT,DELETE,OPTIONS

# Indicate which header field names may be used during the actual
# request. (list value)
#allow_headers = Content-Type,Cache-Control,Content-Language,Expires,Last-Modified,Pragma


[database]

#
# From oslo.db
#

# The file name to use with SQLite. (string value)
# Deprecated group/name - [DEFAULT]/sqlite_db
#sqlite_db = oslo.sqlite

# If True, SQLite uses synchronous mode. (boolean value)
# Deprecated group/name - [DEFAULT]/sqlite_synchronous
#sqlite_synchronous = true

# The back end to use for the database. (string value)
# Deprecated group/name - [DEFAULT]/db_backend
#backend = sqlalchemy

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
#max_overflow = 50

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


[keystone_authtoken]

#
# From keystonemiddleware.auth_token
#

# Complete public Identity API endpoint. (string value)
auth_uri = {{ auth_uri }}
auth_url = {{ auth_url }}

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
memcached_servers = {{ memcached_servers }}

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
# authenticated or authenticated and encrypted. If MAC, token data is
# authenticated (with HMAC) in the cache. If ENCRYPT, token data is
# encrypted and authenticated in the cache. If the value is not one of
# these options or empty, auth_token will raise an exception on
# initialization. (string value)
# Allowed values: None, MAC, ENCRYPT
#memcache_security_strategy = None

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

# Protocol of the admin Identity API endpoint. Deprecated, use
# identity_uri. (string value)
# Allowed values: http, https
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

# Authentication type to load (unknown value)
# Deprecated group/name - [DEFAULT]/auth_plugin
auth_type = password

# Config Section from which to load plugin specific options (unknown
# value)
#auth_section = <None>
project_domain_name = default
user_domain_name = default
project_name = service
username = manila
password = {{ manila_pass }}


[matchmaker_redis]

#
# From oslo.messaging
#

# Host to locate redis. (string value)
#host = 127.0.0.1

# Use this port to connect to redis host. (port value)
# Minimum value: 0
# Maximum value: 65535
#port = 6379

# Password for Redis server (optional). (string value)
#password =

# List of Redis Sentinel hosts (fault tolerance mode) e.g.
# [host:port, host1:port ... ] (list value)
#sentinel_hosts =

# Redis replica set name. (string value)
#sentinel_group_name = oslo-messaging-zeromq

# Time in ms to wait between connection attempts. (integer value)
#wait_timeout = 500

# Time in ms to wait before the transaction is killed. (integer value)
#check_timeout = 20000

# Timeout in ms on blocking socket operations (integer value)
#socket_timeout = 1000


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

# Space separated list of acceptable SASL mechanisms (string value)
# Deprecated group/name - [amqp1]/sasl_mechanisms
#sasl_mechanisms =

# Path to directory that contains the SASL configuration (string
# value)
# Deprecated group/name - [amqp1]/sasl_config_dir
#sasl_config_dir =

# Name of configuration file (without .conf suffix) (string value)
# Deprecated group/name - [amqp1]/sasl_config_name
#sasl_config_name =

# User name for message broker authentication (string value)
# Deprecated group/name - [amqp1]/username
#username =

# Password for message broker authentication (string value)
# Deprecated group/name - [amqp1]/password
#password =


[oslo_messaging_notifications]

#
# From oslo.messaging
#

# The Drivers(s) to handle sending notifications. Possible values are
# messaging, messagingv2, routing, log, test, noop (multi valued)
# Deprecated group/name - [DEFAULT]/notification_driver
#driver =

# A URL representing the messaging driver to use for notifications. If
# not set, we fall back to the same configuration used for RPC.
# (string value)
# Deprecated group/name - [DEFAULT]/notification_transport_url
#transport_url = <None>

# AMQP topic used for OpenStack notifications. (list value)
# Deprecated group/name - [rpc_notifier2]/topics
# Deprecated group/name - [DEFAULT]/notification_topics
#topics = notifications


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

# EXPERIMENTAL: Possible values are: gzip, bz2. If not set compression
# will not be used. This option may notbe available in future
# versions. (string value)
#kombu_compression = <None>

# How long to wait a missing client beforce abandoning to send it its
# replies. This value should not be longer than rpc_response_timeout.
# (integer value)
# Deprecated group/name - [DEFAULT]/kombu_reconnect_timeout
#kombu_missing_consumer_retry_timeout = 60

# Determines how the next RabbitMQ node is chosen in case the one we
# are currently connected to becomes unavailable. Takes effect only if
# more than one RabbitMQ node is provided in config. (string value)
# Allowed values: round-robin, shuffle
#kombu_failover_strategy = round-robin

# The RabbitMQ broker address where a single node is used. (string
# value)
# Deprecated group/name - [DEFAULT]/rabbit_host
#rabbit_host = localhost

# The RabbitMQ broker port where a single node is used. (port value)
# Minimum value: 0
# Maximum value: 65535
# Deprecated group/name - [DEFAULT]/rabbit_port
#rabbit_port = 5672

# RabbitMQ HA cluster host:port pairs. (list value)
# Deprecated group/name - [DEFAULT]/rabbit_hosts
#rabbit_hosts = $rabbit_host:$rabbit_port
rabbit_hosts = {{ rabbit_hosts }}

# Connect over SSL for RabbitMQ. (boolean value)
# Deprecated group/name - [DEFAULT]/rabbit_use_ssl
#rabbit_use_ssl = false

# The RabbitMQ userid. (string value)
# Deprecated group/name - [DEFAULT]/rabbit_userid
rabbit_userid = {{ rabbit_userid }}

# The RabbitMQ password. (string value)
# Deprecated group/name - [DEFAULT]/rabbit_password
rabbit_password = {{ rabbit_password }}

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

# Maximum interval of RabbitMQ connection retries. Default is 30
# seconds. (integer value)
#rabbit_interval_max = 30

# Maximum number of RabbitMQ connection retries. Default is 0
# (infinite retry count). (integer value)
# Deprecated group/name - [DEFAULT]/rabbit_max_retries
#rabbit_max_retries = 0

# Try to use HA queues in RabbitMQ (x-ha-policy: all). If you change
# this option, you must wipe the RabbitMQ database. In RabbitMQ 3.0,
# queue mirroring is no longer controlled by the x-ha-policy argument
# when declaring a queue. If you just want to make sure that all
# queues (except  those with auto-generated names) are mirrored across
# all nodes, run: "rabbitmqctl set_policy HA '^(?!amq\.).*' '{"ha-
# mode": "all"}' " (boolean value)
# Deprecated group/name - [DEFAULT]/rabbit_ha_queues
#rabbit_ha_queues = false

# Positive integer representing duration in seconds for queue TTL
# (x-expires). Queues which are unused for the duration of the TTL are
# automatically deleted. The parameter affects only reply and fanout
# queues. (integer value)
# Minimum value: 1
#rabbit_transient_queues_ttl = 1800

# Specifies the number of messages to prefetch. Setting to zero allows
# unlimited messages. (integer value)
#rabbit_qos_prefetch_count = 0

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

# Maximum number of channels to allow (integer value)
#channel_max = <None>

# The maximum byte size for an AMQP frame (integer value)
#frame_max = <None>

# How often to send heartbeats for consumer's connections (integer
# value)
#heartbeat_interval = 1

# Enable SSL (boolean value)
#ssl = <None>

# Arguments passed to ssl.wrap_socket (dict value)
#ssl_options = <None>

# Set socket timeout in seconds for connection's socket (floating
# point value)
#socket_timeout = 0.25

# Set TCP_USER_TIMEOUT in seconds for connection's socket (floating
# point value)
#tcp_user_timeout = 0.25

# Set delay for reconnection to some host which has connection error
# (floating point value)
#host_connection_reconnect_delay = 0.25

# Maximum number of connections to keep queued. (integer value)
#pool_max_size = 10

# Maximum number of connections to create above `pool_max_size`.
# (integer value)
#pool_max_overflow = 0

# Default number of seconds to wait for a connections to available
# (integer value)
#pool_timeout = 30

# Lifetime of a connection (since creation) in seconds or None for no
# recycling. Expired connections are closed on acquire. (integer
# value)
#pool_recycle = 600

# Threshold at which inactive (since release) connections are
# considered stale in seconds or None for no staleness. Stale
# connections are closed on acquire. (integer value)
#pool_stale = 60

# Persist notification messages. (boolean value)
#notification_persistence = false

# Exchange name for for sending notifications (string value)
#default_notification_exchange = ${control_exchange}_notification

# Max number of not acknowledged message which RabbitMQ can send to
# notification listener. (integer value)
#notification_listener_prefetch_count = 100

# Reconnecting retry count in case of connectivity problem during
# sending notification, -1 means infinite retry. (integer value)
#default_notification_retry_attempts = -1

# Reconnecting retry delay in case of connectivity problem during
# sending notification message (floating point value)
#notification_retry_delay = 0.25

# Time to live for rpc queues without consumers in seconds. (integer
# value)
#rpc_queue_expiration = 60

# Exchange name for sending RPC messages (string value)
#default_rpc_exchange = ${control_exchange}_rpc

# Exchange name for receiving RPC replies (string value)
#rpc_reply_exchange = ${control_exchange}_rpc_reply

# Max number of not acknowledged message which RabbitMQ can send to
# rpc listener. (integer value)
#rpc_listener_prefetch_count = 100

# Max number of not acknowledged message which RabbitMQ can send to
# rpc reply listener. (integer value)
#rpc_reply_listener_prefetch_count = 100

# Reconnecting retry count in case of connectivity problem during
# sending reply. -1 means infinite retry during rpc_timeout (integer
# value)
#rpc_reply_retry_attempts = -1

# Reconnecting retry delay in case of connectivity problem during
# sending reply. (floating point value)
#rpc_reply_retry_delay = 0.25

# Reconnecting retry count in case of connectivity problem during
# sending RPC message, -1 means infinite retry. If actual retry
# attempts in not 0 the rpc request could be processed more then one
# time (integer value)
#default_rpc_retry_attempts = -1

# Reconnecting retry delay in case of connectivity problem during
# sending RPC message (floating point value)
#rpc_retry_delay = 0.25

[oslo_concurrency]
lock_path = /var/lib/manila/tmp
"""