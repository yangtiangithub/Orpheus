# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:44.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import uuid
from chatbot.sessions.queue import ResponseQueue
import time


class Session(object):

    def __init__(self, user_id, maxsize=50):
        self.id = str(uuid.uuid1())

        self.conversation = ResponseQueue(maxsize=maxsize)

        # last
        self.last_conversate_time = int()
        self.last_status = None
        self.last_target = None
        self.last_domain = None