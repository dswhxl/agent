#! /usr/bin/env python
# coding: utf8
"""
agent小程序
"""
import sys
import requests
import web

from src.agent_log import Log
import src.url as m_url
from src.util import Util

# class as apis
from src.api.start_task import StartTask
from src.api.stop_task import StopTask
from src.api.check_task import CheckTask
from src.api.check_online import CheckOnline
from src.api.fetch_words import FetchWords

reload(sys)
sys.setdefaultencoding("utf-8")


def notify_agent():
    """
    desc: 启动时，告知agent的ip:port
    """
    host = Util.get_host()
    port = Util.get_conf()[0]
    notify_url = Util.get_conf()[1]
    payload = {
        "machine_ip": host,
        "machine_port": port,
    }
    print payload
    requests.post(notify_url, params=payload)


if __name__ == "__main__":
    notify_agent()
    app = web.application(m_url.URLS, globals())
    app.run(Log)
