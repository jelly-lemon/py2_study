# encoding:utf-8
import json


def test_1():
    """
    字典转 JSON 字符串

    实际上得到的是 JSON unicode 编号字节串
    """
    d = {u"name": u"绿盟"}
    d = json.dumps(d)  # 返回字节串
    print d


def test_2():
    """
    遍历字典
    """
    d = {u"name": u"绿盟"}
    for k, v in d.items():
        print type(v)


def test_3():
    """
    JSON unicode编号字符串转字典
    """
    s = u'''{"code": "\\u3010\\u7eff\\u76df\\u79d1\\u6280\\u3011\\u9a8c\\u8bc1\\u78015769"}'''
    d = json.loads(s)
    print d
    print d["code"]


def test_4():
    """
    dict 转字符串

    有字典：d = {u"name": u"绿盟"}
    期望将字典转为字符串：u'''{"name": "绿盟"}'''
    直接用 str(d)，却得到：'''{u'name': u'\u7eff\u76df'}'''
    直接用 unicode(d)，却得到：u'''{u'name': u'\u7eff\u76df'}'''
    直接用 json.dumps(d)，却得到：'''{"name": "\u7eff\u76df"}'''
    用 json.dumps(d, ensure_ascii=False)，得到：u'''{{"name": "绿盟"}}'''
    """
    d = {u"name": u"绿盟"}
    # ensure_ascii=False 时，返回 unicode 字符串
    d = json.dumps(d, ensure_ascii=False).encode('utf8')
    print type(d)
    print d


if __name__ == '__main__':
    test_4()
