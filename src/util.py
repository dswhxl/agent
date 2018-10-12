#! /usr/bin/env python
# coding: utf8
"""
Util: 工具类
"""

import ConfigParser
import sys
import subprocess
import src.const as m_const

reload(sys)
sys.setdefaultencoding("utf-8")


class Util(object):
    """
    desc: 处理项目路径的类
    """
    @staticmethod
    def get_conf():
        """
        desc: 读取conf
        """
        cf = ConfigParser.ConfigParser()
        cf.read("./conf/agent.ini")
        try:
            port = int(cf.get(m_const.MODE, "port"))
            notify_url = cf.get(m_const.MODE, "notify_url")
            home = cf.get(m_const.MODE, "home")
        except Exception, e:
            print repr(e)
        return port, notify_url, home

    @staticmethod
    def get_host():
        """
        desc: 获取host
        """
        return subprocess.Popen("hostname -i | awk '{print $NF}'", shell=True, stdout=subprocess.PIPE).stdout.read().strip()


if __name__ == "__main__":
    pass
