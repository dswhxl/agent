#! /usr/bin/env python
# coding: utf8
"""
接口类：CheckTask
"""

import sys
from src.agent_base import AgentBase

reload(sys)
sys.setdefaultencoding("utf-8")


class CheckTask(AgentBase):
    """
    desc: 检查压测实例是否在运行
    """
    def execute(self):
        """
        desc: 主程序
        """
        pid = self.params["pid"]
        ret = self.is_pid_exists(pid)
        if ret:
            res = {"running": 1}
        else:
            res = {"running": 0}
        return self.get_return(res)

if __name__ == "__main__":
    pass
