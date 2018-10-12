#! /usr/bin/python
# coding=utf-8
# author: zhouyou

"""
desc: mysql封装类
"""

import MySQLdb


class MyDb(object):
    """
    mysql封装类
    """
    _conn = None
    _cursor = None

    def __init__(self, host="localhost", user="jenkinsapi", passwd="1q2w3e@sf", db="jenkinsapi_db", charset="utf8", port=3306):
        self._conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db, charset=charset, port=port, ssl="skip-ssl")
        self._cursor = self._conn.cursor()

    def disconnect(self):
        """
        断开连接
        """
        try:
            if self._conn is not None:
                self._cursor.close()
                self._conn.close()
        except Exception, e:
            print repr(e)

    def assemble_select(self, fields, conds, orderby, limits):
        """
        装配select语句
        """
        str_fields = ""
        if isinstance(fields, list):
            str_fields = ", ".join(fields)
        else:
            str_fields = fields
        if not str_fields:
            str_fields = "*"

        str_conds = ""
        if isinstance(conds, list):
            str_conds = " and ".join(conds)
        else:
            str_conds = conds
        if not str_conds:
            str_conds = "WHERE 1=1"
        else:
            str_conds = "WHERE %s" % str_conds

        str_orderby = ""
        if isinstance(orderby, list):
            str_orderby = ", ".join(orderby)
        else:
            str_orderby = orderby
        if str_orderby:
            str_orderby = "ORDER BY %s" % str_orderby

        str_limits = ""
        if limits:
            str_limits = "LIMIT %s" % limits

        return str_fields, str_conds, str_orderby, str_limits


    def my_select(self, table, fields, conds="", orderby="", limits=""):
        """
        select查询
        """
        str_fields, str_conds, str_orderby, str_limits = self.assemble_select(fields, conds, orderby, limits)
        sql = "SELECT %s FROM %s %s %s %s;" % (str_fields, table, str_conds, str_orderby, str_limits)
        self._cursor.execute(sql)

        ret = self._cursor.fetchall()

        return ret

    def assemble_insert(self, fields):
        """
        装配insert语句
        """
        field = {}
        fields_tmp = []
        if isinstance(fields, list):
            field = fields[0]
            fields_tmp = fields
        else:
            field = fields
            fields_tmp.append(fields)
        keys = []
        for key in field:
            keys.append("`%s`" % key)  # 为key加保护
        tmp_key = ", ".join(keys)
        str_key = "(%s)" % tmp_key

        str_value_list = []
        for index in range(len(fields_tmp)):
            values = []
            for key in fields_tmp[index]:
                values.append('\'' + str(fields_tmp[index][key]) + '\'')
            tmp_value = ", ".join(values)
            str_value = "(%s)" % tmp_value
            str_value_list.append(str_value)
        tmp_value = ", ".join(str_value_list)
        str_value = "%s" % tmp_value
        return "%s VALUES %s" % (str_key, str_value)

    def my_insert(self, table, insert_fields):
        """
        执行insert语句
        """
        if not insert_fields:
            return False
        str_fields = self.assemble_insert(insert_fields)
        sql = "INSERT INTO %s %s;" % (table, str_fields)
        ret = self._cursor.execute(sql)
        if ret == 0:
            return False
        self._conn.commit()
        return ret

    def assemble_insert_multi(self, fields):
        """
        装配批量插入语句
        """
        keys = []
        values = []

        for key in fields:
            keys.append(key)
            values.append(fields[key])
        tmp_key = ", ".join(keys)
        str_key = "(%s)" % tmp_key

        str_values = []
        for each in values:
            each = ["'%s'" % i for i in each]
            str_values.append(each)

        row = len(str_values[0])
        row_str = []
        for i in range(row):
            tmp = [j[i] for j in str_values]
            tmp = ", ".join(tmp)
            tmp = "(" + tmp + ")"
            row_str.append(tmp)
        final_str = ", ".join(row_str)
        return "%s VALUES %s" % (str_key, final_str)

    def my_insert_multi(self, table, insert_fields):
        """
        一次插入多条语句
        形如：insert_fields = {
            "order_id", [1,2],
            "name", ["zhouyou", "wenhui"]
        }
        """
        if not insert_fields:
            return False
        str_fields = self.assemble_insert_multi(insert_fields)
        sql = "INSERT INTO %s %s;" % (table, str_fields)
        ret = self._cursor.execute(sql)
        self._conn.commit()
        if ret != 1:
            return False
        return ret

    def assemble_delete(self, conds):
        """
        装配delete语句
        """
        return "WHERE %s" % " and ".join(conds)

    def my_delete(self, table, conds):
        """
        执行delete语句
        """
        str_conds = self.assemble_delete(conds)
        sql = "DELETE FROM %s %s;" % (table, str_conds)
        ret = self._cursor.execute(sql)
        self._conn.commit()
        if ret != 1:
            return False
        return ret

    def assemble_update(self, update_fields, conds):
        """
        装配update语句
        """
        str_fields = "SET %s" % ", ".join(update_fields)
        str_conds = "WHERE %s" % " and ".join(conds)
        return str_fields, str_conds

    def my_update(self, table, update_fields, conds):
        """
        执行update语句
        """
        str_fields, str_conds = self.assemble_update(update_fields, conds)
        sql = "UPDATE %s %s %s;" % (table, str_fields, str_conds)
        ret = self._cursor.execute(sql)
        self._conn.commit()
        if ret != 1:
            return False
        return ret

    def my_query(self, sql, typ="select"):
        """
        通用sql查询
        """
        ret = self._cursor.execute(sql)

        if typ.tolower().strip() == "select":
            ret = self._cursor.fetchall()
        self._conn.commit()

        return ret


if __name__ == "__main__":
    pass
