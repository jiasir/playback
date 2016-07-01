from fabric.api import *
from fabric.tasks import Task
from playback import common

class MysqlManage(common.Common):
    """Manage Galera Cluster for MySQL"""

    def _start_wsrep_new_cluster(self):
        if self._release() == 'xenial':
            result = sudo('systemctl start mysql --wsrep-new-cluster', warn_only=True)
            if result.failed:
                sudo('service mysql start --wsrep-new-cluster')
        else:
            sudo('service mysql start --wsrep-new-cluster')

    def _start_mysql(self):     
        if self._release() == 'xenial':
            sudo('systemctl start mysql')
        else:
            sudo('service mysql start')

    def _stop_mysql(self):
        if self._release() == 'xenial':
            sudo('systemctl stop mysql')
        else:
            sudo('service mysql stop')

    def _change_root_password(self, pwd):
        sudo('mysqladmin -uroot password %s' % pwd)

