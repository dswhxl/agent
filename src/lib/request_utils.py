#! /usr/bin/python
# coding=utf-8
# author: zhouyou

"""
desc: request封装类
"""

import requests


class HttpRequestUtil(object):
    """
    desc: request封装类
    """
    _header = None
    _result = None

    def __init__(self):
        self.reset()

    def reset(self):
        """
        初始化，清空herder和result
        """
        self._header = None
        self._result = None

    def get_header(self):
        """
        获取header
        """
        return self._header

    def get_result(self):
        """
        获取result
        """
        return self._result

    def custom_request(self, method, url, payload=None, headers=None, cookies=None, timeout=30):
        """
        通用request方法
        """
        method = method.tolower(method).strip()
        self.reset()

        res = None
        if method == "get":
            res = requests.get(url, params=payload, headers=headers, cookies=cookies, timeout=timeout)
        elif method == "post":
            res = requests.post(url, data=payload, headers=headers, cookies=cookies, timeout=timeout)
        elif method == "put":
            res = requests.put(url, data=payload, headers=headers, cookies=cookies, timeout=timeout)
        elif method == "delete":
            res = requests.delete(url, headers=headers, cookies=cookies, timeout=timeout)
        elif method == "head":
            res = requests.head(url, headers=headers, cookies=cookies, timeout=timeout)
        elif method == "options":
            res = requests.options(url, headers=headers, cookies=cookies, timeout=timeout)
        return res

    def http_get(self, url, payload=None, headers=None, cookies=None, timeout=30):
        """
        get方法，允许传入url，payload，headers，cookies
        payload默认是str，使用json.dumps(payload)来进行json的转换
        """
        return self.custom_request('get', url, payload=payload, headers=headers, cookies=cookies, timeout=timeout)

    def http_post(self, url, payload=None, headers=None, cookies=None, timeout=30):
        """
        post方法，允许传入url，payload，headers，cookies
        payload默认是str，使用json.dumps(payload)来进行json的转换
        """
        return self.custom_request('post', url, payload=payload, headers=headers, cookies=cookies, timeout=timeout)

    def http_put(self, url, payload=None, headers=None, cookies=None, timeout=30):
        """
        put方法，允许传入url，payload，headers，cookies
        payload默认是str，使用json.dumps(payload)来进行json的转换
        """
        return self.custom_request('put', url, payload=payload, headers=headers, cookies=cookies, timeout=timeout)

    def http_delete(self, url, headers=None, cookies=None, timeout=30):
        """
        delete方法，允许传入url, headers，cookies
        """
        return self.custom_request('delete', url, headers=headers, cookies=cookies, timeout=timeout)


if __name__ == "__main__":
    pass
