#! /usr/bin/env python
# coding: utf8
"""
接口类：CheckOnline
"""

import sys

from src.agent_base import AgentBase
from src.util import Util

reload(sys)
sys.setdefaultencoding("utf-8")


class CheckOnline(AgentBase):
    """
    desc: 检查agent是否在线
    """
    def execute(self):
        """
        desc: 主程序
        """
        host = Util.get_host()
        port = Util.get_conf()[0]
        self.logger.info("host is: %s" % host)
        return self.get_return({"online": 1, "host": host, "port": port})

if __name__ == "__main__":
    pass
