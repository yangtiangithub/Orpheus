# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午5:07.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import jieba

class Preprocessor(object):

    def __init__(self, configs):

        # 初始化jieba分词词表

        # 初始化依存句法分析工具

        # 初始化词表

        pass

    def process(self, stmt):
        """
        对句子进行初始化处理，包括分词、依存句法分析、情感分析等等。
        """
        stmt.set_split_text(self.segment(stmt.text))

        stmt.set_emotion(self.emotion_analysis(stmt.text, None))

        return stmt

    def segment(self, text, cut_all=False, HMM=True):
        return list(jieba.cut(text, cut_all=cut_all, HMM=HMM))

    def dependency_parse(self, text):
        # 调用pyltp进行依存句法分析
        return None

    def emotion_analysis(self, text, contexts):
        # 返回情感分析结果
        return None