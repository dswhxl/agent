#! /usr/bin/env python
# coding: utf8
"""
agent_log：日志处理
"""
import logging
import sys
from wsgilog import WsgiLog
reload(sys)
sys.setdefaultencoding("utf-8")


LOG_FILE = "./log/agent.log"
LOG_FORMAT = "[%(asctime)s] %(filename)s:%(lineno)d(%(funcName)s): [%(levelname)s] %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = logging.DEBUG
INTERVAL = 'd'
BACKUPS = 3


class Log(WsgiLog):
    """
    desc: log类
    """
    def __init__(self, application):
        WsgiLog.__init__(
            self,
            application,
            logformat=LOG_FORMAT,
            datefmt=DATE_FORMAT,
            tofile=True,
            file=LOG_FILE,
            interval=INTERVAL,
            backups=BACKUPS
            )

    def test(self):
        """
        desc: test
        """
        pass


if __name__ == "__main__":
    pass
