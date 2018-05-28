# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:50.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
from chatbot.sessions.user import User


class Manager(object):

    def __init__(self, configs):

        # self.db_conection = None
        # self.cursor = None

        self.user_session = {}
        self.session_list = {}

    def new_user(self):
        u = User()


