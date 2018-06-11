# -*- coding:utf-8 -*-
"""
Created on 18/6/11 下午6:08.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import aiml

class AimlNLG(object):

    def __init__(self, configs):
        self.configs = configs

        self.aiml = aiml.Kernel()
        self.aiml.learn("./aiml/nlg-startup.xml")
        self.aiml.respond("load aiml cn")

    def process(self, status, target, policy):
        response = self.aiml.respond(target)

        return response