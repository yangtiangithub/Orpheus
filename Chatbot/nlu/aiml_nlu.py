# -*- coding:utf-8 -*-
"""
Created on 18/6/11 下午5:35.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import aiml

class AimlNLU(object):

    def __init__(self, configs):
        self.configs = configs

        self.aiml = aiml.Kernel()
        self.aiml.learn("./aiml/nlu-startup.xml")
        self.aiml.respond("load aiml cn")

    def process(self, stmt):
        res = self.aiml.respond(stmt.text)

        if "Greeting" in res:
            return "Greeting", None
        else:
            return None, None