from fabric.api import *
from playback import common

class Cmd(common.Common):
    """Run command line on the target host"""

    def _cmd(self, command_line):
        sudo(command_line, warn_only=True)

    def cmd(self, command_line):
        execute(self._cmd, command_line)
