# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午5:04.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import aiml
from chatbot.utils.preprocessor import Preprocessor
from chatbot.sessions.manager import Manager
from chatbot.sessions.statement import Statement


class Chatbot(object):

    def __init__(self, configs):

        self.name = configs.name
        self.preprocessor = Preprocessor(configs)

        self.aiml = aiml.Kernel()
        # self.aiml.learn
        # self.aiml.respond

        self.sess_manager = Manager(configs)

    def preprocess(self, sentence, sess):

        stmt = self.preprocessor.process(Statement(text=sentence, from_user=True))

        return stmt

    def _get_user(self):
        return None

    def _get_sess(self):
        return None, None

    def listen(self, sentence):
        user = self._get_user()
        sess, sess_id = self._get_sess()

        stmt = self.preprocess(sentence, sess)

        _, _, _, _ = self.get_response(stmt, sess)

        # 判断任务是否完成

        return None, None, None, None

    def get_response(self, stmt, sess):
        return None, None, None, None