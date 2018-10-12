#! /usr/bin/env python
# coding: utf8
"""
Path: 处理项目路径的类
"""

import sys
from src.util import Util

reload(sys)
sys.setdefaultencoding("utf-8")


class Path(object):
    """
    desc: 处理项目路径的类
    """
    @staticmethod
    def get_workspace():
        """
        desc: 获取workspace路径
        """
        confs = Util.get_conf()
        return "%s/performance/workspace" % confs[2]


if __name__ == "__main__":
    pass
