#! /usr/bin/env python
# coding: utf8
"""
agent小程序
"""

import os
import sys
import src.error_code as m_error_code
from src.agent_base import AgentBase

reload(sys)
sys.setdefaultencoding("utf-8")


class StopTask(AgentBase):
    """
    desc: 通过pid, 停止jmeter服务
    """
    def execute(self):
        """
        desc: 主程序
        """
        pid = self.params["pid"]
        self.kill_pid(pid)
        os.system("sh refresh_defunct_pid.sh")      # 我也很无奈，为了刷掉一个僵尸进程

        ret = self.is_pid_killed(pid)
        if not ret:
            errno = m_error_code.ERR_CODE_STOP_JMETER_FAIL
            errmsg = u"stop jmeter fail"
            ret = self.get_return({}, errno, errmsg)
        else:
            ret = self.get_return()

        return ret

if __name__ == "__main__":
    pass
