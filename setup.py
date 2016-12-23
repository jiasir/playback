# The MIT License (MIT)
#
# Copyright (c) 2015-2016 Taio Jia (jiasir) <jiasir@icloud.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    print("playback now needs setuptools in order to build. Install it using"
          " your package manager (usually python-setuptools) or via pip (pip"
          " install setuptools).")
    sys.exit(1)

from playback import __version__ as VERSION
from playback import __author__ as AUTHOR

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        f = open(path)
    except IOError:
        return None
    return f.read()

setup(name='playback',
    version=VERSION,
    description='OpenStack provisioning and orchestration library with command-line tools',
    long_description=read('README.md'),
    author=AUTHOR,
    author_email='jiasir@icloud.com',
    url='https://github.com/jiasir/playback/',
    license='MIT',
    install_requires=['cliff==2.3.0', 'fabric == 1.10.2', 'ecdsa == 0.13', 'markupsafe == 0.23', 'paramiko == 1.16.0', 'jinja2 == 2.8', 'PyYAML == 3.11', 'setuptools == 19.6.2', 'pycrypto == 2.6.1', 'tqdm == 3.8.0'],
    packages=find_packages(),
    entry_points={
       'console_scripts': [
           'playback = playback.cli.main:main',
        ],
        'cliff.playback': [
            'environment = playback.cli.environment:make',
            'mysql = playback.cli.mysql:make',
            'haproxy = playback.cli.haproxy:make',
            'rabbitmq = playback.cli.rabbitmq:make',
            'keystone = playback.cli.keystone:make',
            'glance = playback.cli.glance:make',
            'nova = playback.cli.nova:make',
            'nova-compute = playback.cli.nova_compute:make',
            'neutron = playback.cli.neutron:make',
            'neutron-agent = playback.cli.neutron_agent:make',
            'horizon = playback.cli.horizon:make',
            'cinder = playback.cli.cinder:make',
            'swift = playback.cli.swift:make',
            'swift-storage = playback.cli.swift_storage:make',
            'manila = playback.cli.manila:make',
            'manila-share = playback.cli.manila_share:make'
        ],
       },
    )
