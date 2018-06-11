# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午4:30.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""

class Statement(object):

    def __init__(self,
                 text,
                 from_user=True):

        self.text = text
        self.from_user = from_user
        self.context = None

        self.split_text = None
        self.emotion = None

    def set_split_text(self, split_text):
        self.split_text = split_text

    def get_split_text(self):
        return self.split_text

    def set_emotion(self, emotion):
        self.emotion = emotion

    def get_emotion(self):
        return self.emotion