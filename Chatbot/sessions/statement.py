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

        self.segment = None
        self.pos = None
        self.emotion = None

        self.from_user = from_user


    def set_segment(self, segment):
        self.segment = segment

    def get_segment(self):
        return self.segment

    def set_emotion(self, emotion):
        self.emotion = emotion

    def get_emotion(self):
        return self.emotion

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos