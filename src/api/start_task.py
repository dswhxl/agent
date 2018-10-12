#! /usr/bin/env python
# coding: utf8
"""
接口类：StartTask
"""

import sys
import src.error_code as m_error_code
from src.agent_base import AgentBase
from src.agent_base import AgentException

reload(sys)
sys.setdefaultencoding("utf-8")


class StartTask(AgentBase):
    """
    desc: 启动jmeter实例，开始压测服务
    """
    def execute(self):
        """
        desc: 主程序
        """
        self.generateCfg()

        cmd = self.params["cmd"]
        pid = self.run_cmd(cmd)
        ret = self.is_pid_started(pid)
        if not ret:
            errno = m_error_code.ERR_CODE_START_JMETER_FAIL
            errmsg = u"start jmeter fail"
            ret = self.get_return({}, errno, errmsg)
        else:
            ret = self.get_return({"pid": pid})
        return ret


    def generateCfg(self):
        """
        desc: 将二进制字节流保存为配置文件
        """
        try:
            file_name = self.params["cfg"]["name"]
            file_content = self.params["cfg"]["content"]
        except Exception, e:
            raise AgentException(e)
        file_path = "../workspace/%s/jmxs/%s" % (self.task_id, file_name)
        self.logger.info("file path is: %s" % file_path)
        try:
            open(file_path, "wb").write(file_content)
        except Exception, e:
            raise AgentException(e)

if __name__ == "__main__":
    pass
