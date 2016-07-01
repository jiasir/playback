from fabric.api import *
from fabric.contrib import files
import os
from playback.templates.my_cnf import conf_my_cnf
from playback import common
from fabric.tasks import Task

class MysqlConfig(Task, common.Common):
    """Setup Galera Cluster for MySQL"""

    def __init__(self, user, hosts=None, key_filename=None, password=None, parallel=True, *args, **kwargs):
        super(MysqlConfig, self).__init__(*args, **kwargs)
        self.user = user
        self.hosts = hosts
        self.parallel = parallel
        self.key_filename = key_filename
        self.password = password
        env.user = self.user
        env.hosts = self.hosts
        env.parallel = self.parallel
        env.key_filename = self.key_filename
        env.password = self.password
        env.abort_on_prompts = False

    def _update_mysql_config(self, wsrep_cluster_address, wsrep_node_name, wsrep_node_address):
        with open('tmp_my_cnf_'+env.host_string, 'w') as f:
            f.write(conf_my_cnf)
        files.upload_template(filename='tmp_my_cnf_'+env.host_string, 
                              destination='/etc/mysql/my.cnf', 
                              context={'wsrep_cluster_address': wsrep_cluster_address, 
                                       'wsrep_node_name': wsrep_node_name, 
                                       'wsrep_node_address': wsrep_node_address}, 
                              use_jinja=True, use_sudo=True, backup=True)
        try:
            os.remove('tmp_my_cnf_'+env.host_string)
        except Exception:
            pass