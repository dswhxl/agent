#! /usr/bin/env python
# coding: utf8
"""
接口类FetchWords
"""

import os
import sys
from src.agent_base import AgentBase
from src.path import Path

reload(sys)
sys.setdefaultencoding("utf-8")


class FetchWords(AgentBase):
    """
    desc: 获取词表
    """
    def execute(self):
        """
        desc: 主程序
        """
        workspace = Path.get_workspace()
        for item in self.params["download"]:
            cmd_download = "curl -o %s/%s/words/%s %s" % (workspace, self.task_id, item["name"], item["url"])
            self.logger.info("cmd download is: %s" % cmd_download)
            os.system(cmd_download)
        return self.get_return()


if __name__ == "__main__":
    pass
