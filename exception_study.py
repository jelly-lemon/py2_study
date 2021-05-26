#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python2 中，必须指定 file coding



def test_0():
    """
    捕获异常
    """
    try:
        n = int("abc")
    # 【易错点】except 这里和 python3 写法不同
    except Exception, err:
        print(err)