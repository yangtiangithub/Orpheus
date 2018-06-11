# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:50.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
from Chatbot.sessions.user import User
from Chatbot.sessions.session import Session


class Manager(object):

    def __init__(self, configs):

        # self.db_conection = None
        # self.cursor = None

        self.user_session = {}
        self.session_list = {}

    def new_user(self):
        u = User()

    def get_user(self):
        pass

    def new_session(self, user):
        session = Session(user.uid)
        self.user_session[user.uid] = session
        self.session_list[session.id] = session

    def get_session_by_sid(self, session_id, default=None):
        return self.session_list.get(str(session_id), default)

    def get_session_by_uid(self, user_id, default=None):
        return self.user_session.get(str(user_id), default)

    def update_session_domain(self, session_id, domain):
        self.session_list[session_id].last_domain = domain

    def update_session_target(self, session_id, target):
        self.session_list[session_id].last_target = target

    def update_session_status(self, session_id, status):
        self.session_list[session_id].last_status = status
