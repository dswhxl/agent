#! /usr/bin/env python
# coding=utf-8
# author: zhouyou

"""
desc: logging类封装
"""

import ConfigParser
import logging


class SfLog(object):
    """
    desc: log类
    """
    def __init__(self):
        pass

    @staticmethod
    def get_level_by_level_num(level_num):
        """
        根据level number获取日志level
        """
        level_mapping = {
            "16": logging.DEBUG,
            "8": logging.INFO,
            "4": logging.WARNING,
            "2": logging.ERROR,
            "1": logging.CRITICAL,
        }
        return level_mapping.get(level_num, logging.INFO)

    @staticmethod
    def debug(msg):
        """
        打debug日志
        """
        mode = "prod"
        cfhandler = ConfigParser.ConfigParser()
        cfhandler.read("conf/log.ini")
        filename = cfhandler.get(mode, "filepath_debug")
        level_num = cfhandler.get(mode, "level")
        level = SfLog.get_level_by_level_num(level_num)

        SfLog.logger = logging.getLogger(filename)
        SfLog.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')

        SfLog.logger.setLevel(level)

        SfLog.file_handler = logging.FileHandler(filename)
        SfLog.file_handler.setFormatter(SfLog.formatter)
        SfLog.file_handler.setLevel(level)

        if not SfLog.logger.handlers:
            SfLog.logger.addHandler(SfLog.file_handler)

        SfLog.logger.debug(msg)


    @staticmethod
    def info(msg):
        """
        打info日志
        """
        mode = "prod"
        cfhandler = ConfigParser.ConfigParser()
        cfhandler.read("conf/log.ini")
        filename = cfhandler.get(mode, "filepath_info")
        level_num = cfhandler.get(mode, "level")
        level = SfLog.get_level_by_level_num(level_num)

        SfLog.logger = logging.getLogger(filename)
        SfLog.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')

        SfLog.logger.setLevel(level)

        SfLog.file_handler = logging.FileHandler(filename)
        SfLog.file_handler.setFormatter(SfLog.formatter)
        SfLog.file_handler.setLevel(level)

        if not SfLog.logger.handlers:
            SfLog.logger.addHandler(SfLog.file_handler)

        SfLog.logger.info(msg)


    @staticmethod
    def warning(msg):
        """
        打warning日志
        """
        mode = "prod"
        cfhandler = ConfigParser.ConfigParser()
        cfhandler.read("conf/log.ini")
        filename = cfhandler.get(mode, "filepath_warning")
        level_num = cfhandler.get(mode, "level")
        level = SfLog.get_level_by_level_num(level_num)

        SfLog.logger = logging.getLogger(filename)
        SfLog.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')

        SfLog.logger.setLevel(level)

        SfLog.file_handler = logging.FileHandler(filename)
        SfLog.file_handler.setFormatter(SfLog.formatter)
        SfLog.file_handler.setLevel(level)

        if not SfLog.logger.handlers:
            SfLog.logger.addHandler(SfLog.file_handler)

        SfLog.logger.warning(msg)


    @staticmethod
    def error(msg):
        """
        打error日志
        """
        mode = "prod"
        cfhandler = ConfigParser.ConfigParser()
        cfhandler.read("conf/log.ini")
        filename = cfhandler.get(mode, "filepath_error")
        level_num = cfhandler.get(mode, "level")
        level = SfLog.get_level_by_level_num(level_num)

        SfLog.logger = logging.getLogger(filename)
        SfLog.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')

        SfLog.logger.setLevel(level)

        SfLog.file_handler = logging.FileHandler(filename)
        SfLog.file_handler.setFormatter(SfLog.formatter)
        SfLog.file_handler.setLevel(level)

        if not SfLog.logger.handlers:
            SfLog.logger.addHandler(SfLog.file_handler)

        SfLog.logger.error(msg)


    @staticmethod
    def critical(msg):
        """
        打critical日志
        """
        mode = "prod"
        cfhandler = ConfigParser.ConfigParser()
        cfhandler.read("conf/log.ini")
        filename = cfhandler.get(mode, "filepath_critical")
        level_num = cfhandler.get(mode, "level")
        level = SfLog.get_level_by_level_num(level_num)

        SfLog.logger = logging.getLogger(filename)
        SfLog.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')

        SfLog.logger.setLevel(level)

        SfLog.file_handler = logging.FileHandler(filename)
        SfLog.file_handler.setFormatter(SfLog.formatter)
        SfLog.file_handler.setLevel(level)

        if not SfLog.logger.handlers:
            SfLog.logger.addHandler(SfLog.file_handler)

        SfLog.logger.critical(msg)


def test():
    """
    test this module
    """
    SfLog.debug("this is debug")
    SfLog.info("this is info")
    SfLog.warning("this is warning")
    SfLog.error("this is error")
    SfLog.critical("this is critical")


if __name__ == "__main__":
    test()
