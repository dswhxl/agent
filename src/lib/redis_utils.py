#! /usr/bin/env python
# coding=utf-8
# author: zhouyou

"""
desc: 封装的Redis类
"""

import redis


class SfRedis(object):
    """
    desc: redis类
    """
    def __init__(self, host="localhost", port=6379, db=0):
        self._conn = redis.Redis(host=host, port=port, db=db)

    @staticmethod
    def assert_true(flag):
        """断言为真"""
        if flag is False:
            raise Exception("assert fails.")

    def get_redis_string(self, key):
        """获取string类型的redis指定key的值"""
        key = key.strip()
        self.assert_true(isinstance(key, (unicode, str)))
        return self._conn.get(key)

    def get_redis_multi_string(self, keys):
        """获取string类型的redis多个key的值"""
        self.assert_true(isinstance(keys, list))
        return self._conn.mget(keys)

    def set_redis_string(self, key_values):
        """设置string类型的redis多个key的值"""
        self.assert_true(isinstance(key_values, dict))
        return self._conn.mset(key_values)

    def get_redis_hash(self, key, field):
        """获取hash类型的redis某个key，某个field的值"""
        key = key.strip()
        field = field.strip()
        self.assert_true(isinstance(key, (unicode, str)))
        self.assert_true(isinstance(field, (unicode, str)))
        return self._conn.hget(key, field)

    def get_redis_multi_hash(self, key, fields):
        """获取hash类型的redis某个key，多个fields的值"""
        key = key.strip()
        self.assert_true(isinstance(key, (unicode, str)))
        self.assert_true(isinstance(fields, list))
        return self._conn.hmget(key, fields)

    def get_redis_all_hash(self, key):
        """获取hash类型的redis某个key，所有fields的值"""
        key = key.strip()
        self.assert_true(isinstance(key, (unicode, str)))
        return self._conn.hgetall(key)

    def set_redis_multi_hash(self, key, field_values):
        """设置hash类型的redis某个key，多个fields"""
        key = key.strip()
        self.assert_true(isinstance(key, (unicode, str)))
        self.assert_true(isinstance(field_values, dict))
        return self._conn.hmset(key, field_values)

    def del_redis_key(self, key):
        """删除redis中的某一个key"""
        key = key.strip()
        return self._conn.delete(key)


if __name__ == "__main__":
    pass
