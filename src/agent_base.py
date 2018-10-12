#! /usr/bin/env python
# coding: utf8
"""
AgentBase： 基类
"""

import json
import os
import subprocess
import web

import src.error_code as m_error_code
from src.util import Util


class AgentException(Exception):
    """
    desc: 自定义异常类
    """
    pass


class AgentBase(object):
    """
    desc: 基类
    """

    def __init__(self):
        """
        desc: 初始化
        """
        self.logger = web.ctx.environ['wsgilog.logger']
        web.config.debug = False
        self.data = web.input()

    def POST(self):
        """
        desc: post基类
        """
        try:
            self.prepare()
            res = self.execute()
        except Exception, e:
            self.logger.error(repr(e))
            return self.get_return({}, m_error_code.ERR_CODE_SYSTEM, repr(e))
        return res

    def execute(self):
        """
        desc: execute主逻辑
        """
        pass

    def prepare(self):
        """
        desc: prepare：解压入参数据，初始化环境变量，目录等
        """
        home = Util.get_conf()[2]
        self.decouple_data()
        self.logger.info("action is: %s" % self.action)
        self.logger.info("desc is: %s" % self.desc)
        self.logger.info("task_id is: %s" % self.task_id)
        self.logger.info("params is %s" % json.dumps(self.params))
        self.logger.info("import env variables in .bashrc.")
        subprocess.Popen("source %s/.bashrc" % home, shell=True)
        self.logger.info('init dirs.')
        os.system("/bin/sh init_task.sh %s" % self.task_id)

    def decouple_data(self):
        """
        desc: 解压数据
        """
        try:
            self.action = self.data.get("action")
            self.desc = self.data.get("desc")
            self.task_id = self.data.get("task_id")
            self.params = json.loads(self.data.get("params"))
        except Exception, e:
            raise AgentException(e)

    def get_return(self, data={}, errno=0, errmsg="success"):
        """
        desc: 组装返回值
        """
        ret = {
            "errno" : errno,
            "errmsg": errmsg,
            "data": data
        }
        return json.dumps(ret)

    def run_cmd(self, cmd):
        """
        desc: 运行cmd，并获取pid
        """
        self.logger.info("cmd is running: %s" % cmd)
        p = subprocess.Popen(cmd, shell=True)
        pid = int(p.pid)
        return pid

    def kill_pid(self, pid, iterative=True):
        """
        desc: kill pid
        """
        if iterative:
            cmd_kill_with_children = "ps -ef | grep %s | grep -v grep | awk '{print $2, $3}' | grep %s | awk '{print $1}' | xargs kill -9" % (pid, pid)
            self.logger.info("cmd is running: %s" % cmd_kill_with_children)
            subprocess.Popen(cmd_kill_with_children, shell=True)
        else:
            subprocess.Popen("kill -9 %s" % pid, shell=True)

    def is_pid_exists(self, pid):
        """
        desc: 判断pid是否活着
        """
        cmd = "ps -ef | grep %s | grep -v grep | awk '{print $2}' | grep %s | wc -l" % (pid, pid)
        self.logger.info("cmd is running: %s" % cmd)
        ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().strip()
        if int(ret) == 0:
            return False
        return True

    def is_pid_started(self, pid):
        """
        desc: 判断pid是否启动了
        """
        return self.is_pid_exists(pid)

    def is_pid_killed(self, pid):
        """
        desc: 判断pid是否杀死了
        """
        return not self.is_pid_exists(pid)


if __name__ == "__main__":
    pass
