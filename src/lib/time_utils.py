#! /usr/bin/python
# coding=utf-8
# author: zhouyou

"""
desc: time封装类
"""

import datetime
import time


class SfTime(object):
    """
    desc: time封装类
    """
    @staticmethod
    def transform_date2datetime(o_date):
        """
        将date对象转化为datetime对象
        """
        str_time = o_date.strftime("%Y%m%d")
        o_datetime = datetime.datetime.strptime(str_time, "%Y%m%d")
        return o_datetime

    @staticmethod
    def get_today(fmt="%Y%m%d"):
        """
        获取今天的年月日表示，可定义格式
        """
        today = datetime.date.today()
        return today.strftime(fmt)

    @staticmethod
    def get_this_monday(fmt="%Y%m%d"):
        """
        获取本周周一的年月日表示，可定义格式
        """
        today = datetime.date.today()
        delta = today.weekday()
        monday = today - datetime.timedelta(days=delta)
        return monday.strftime(fmt)

    @staticmethod
    def get_last_monday(fmt="%Y%m%d"):
        """
        获取上周周一的年月日表示，可定义格式
        """
        today = datetime.date.today()
        delta = today.weekday()+7
        monday = today - datetime.timedelta(days=delta)
        return monday.strftime(fmt)

    @staticmethod
    def get_today_week_day():
        """
        获取今天是周几，返回0~6分别表示周一~周日
        """
        return datetime.date.today().weekday()

    @staticmethod
    def get_someday_start_second(o_date):
        """
        获取某天00:00开始的秒数
        """
        o_datetime = SfTime.transform_date2datetime(o_date)
        return int(time.mktime(o_datetime.timetuple()))

    @staticmethod
    def get_today_start_second():
        """
        获取今天开始的秒数
        """
        today = datetime.date.today()
        return SfTime.get_someday_start_second(today)

    @staticmethod
    def check_if_today_first_weekday_in_this_month(some_day=None):
        """
        检查今天是不是本月第一个工作日
        """
        # 如果今天是周末，直接返回False
        if some_day is None:
            some_day = datetime.date.today()
        if some_day.weekday() in (5, 6):
            return False

        # 如果今天以前的任意一天（本月），是工作日，返回False
        today_day = some_day.day
        for back in range(1, today_day):        # 往前推1~today-1天，可以推到本月1号
            tmp_day = some_day - datetime.timedelta(days=back)
            if tmp_day.weekday() in (0, 1, 2, 3, 4):
                return False
        return True

    @staticmethod
    def check_if_today_weekday_after_one_week_in_this_month(some_day=None):
        """
        检查今天是不是本月一周后的首个工作日, 也就是说，离本月首个工作日相距7天
        """
        # 只要检查7天前是不是本月第一个工作日即可
        if some_day is None:
            some_day = datetime.date.today()
        today_before_7 = some_day - datetime.timedelta(days=7)
        return SfTime.check_if_today_first_weekday_in_this_month(today_before_7)


if __name__ == "__main__":
    pass
