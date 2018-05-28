# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:28.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class User(object):

    def __init__(self, uid=None, uname=None):

        self.uid = uid
        self.uname = uname
        self.umodel = None