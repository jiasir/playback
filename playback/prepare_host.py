import os

from fabric.api import *
from fabric.colors import red
from fabric.contrib import files
from fabric.tasks import Task

from playback import common
from playback.templates.external_interface import conf_external_interface


class PrepareHost(common.Common):
    """
    Prepare the OpenStack environment

    :param user(str): the user for remote server to login
    :param hosts(list): this is a second param
    :param key_filename(str): the ssh private key to used, default None
    :param password(str): the password for remote server
    :param parallel(bool): paralleler execute on remote server, default True
    :returns: None
    :Examples:

        .. code-block:: python

            # create an instance of PrepareHost
            p = PrepareHost(
                user='ubuntu',
                hosts=['haproxy1','haproxy2','controller1','controller2','compute1','compute2','compute3','compute4']
                )

            # setup the external interface
            p.setup_external_interface(public_interface='eth1')

            # setup ntp
            p.setup_ntp()

            # setup repo
            p.setup_openstack_repository()
    """

    def _setup_external_interface(self, public_interface):
        print red(env.host_string + ' | Setup public interface')
        with open('tmp_public_interface_cfg_' + env.host_string, 'w') as f:
            f.write(conf_external_interface)
        files.upload_template(filename='tmp_public_interface_cfg_' + env.host_string,
                              destination='/etc/network/interfaces.d/public_interface.cfg',
                              use_jinja=True,
                              use_sudo=True,
                              backup=True,
                              context={
                                  'public_interface': public_interface
                              })
        os.remove('tmp_public_interface_cfg_' + env.host_string)

    def setup_external_interface(self, *args, **kwargs):
        """
        host networking

        :param public_interface(str): the public interface
        :returns: None
        """
        return execute(self._setup_external_interface, *args, **kwargs)

    def _setup_ntp(self):
        """network time protocal (ntp)"""
        sudo('echo \'Asia/Shanghai\' | sudo tee /etc/timezone')
        sudo('cat /usr/share/zoneinfo/Asia/Shanghai | sudo tee /etc/localtime')
        sudo('apt-get update')
        sudo('apt-get install chrony -y')
        # TODO: setup ntp server and ntp client, current all are clients

    def setup_ntp(self):
        """
        Setup ntp service

        :returns: None
        """
        return execute(self._setup_ntp)

    def _set_openstack_repository(self):
        """openstack packages"""
        if self._release() == 'trusty':
            print red(env.host_string + ' | Enable the OpenStack repository for trusty')
            sudo('apt-get update')
            sudo('apt-get install software-properties-common -y')
            sudo('add-apt-repository cloud-archive:mitaka -y')

        print red(env.host_string + ' | Executing dist-upgrade')
        with prefix('sudo apt-get update'):
            sudo('DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade')

        print red(env.host_string + ' | [Playback] waiting for reboot\n')
        with settings(warn_only=True):
            reboot(wait=600)

        print red(env.host_string + ' | Install the OpenStack client')
        with prefix('sudo apt-get update'):
            sudo('apt-get install python-openstackclient -y')

    def set_openstack_repository(self):
        """
        Install OpenStack repository only for trusty.

        This method install cloud-archive:mitaka on trusty, when xenial using the default xenial repo.

        :returns: None
        """
        return execute(self._set_openstack_repository)
