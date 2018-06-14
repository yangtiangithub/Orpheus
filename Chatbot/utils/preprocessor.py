# -*- coding:utf-8 -*-
"""
Created on 18/5/28 下午5:07.

Author: Ruizhang1993 (zhang1rui4@foxmail.com)
"""
import pyltp
import jieba.posseg as pseg

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

        # 分词和词性标注
        seg, pos = self.cut(stmt.text)
        stmt.set_segment(seg)
        stmt.set_pos(pos)

        stmt.set_emotion(self.emotion_analysis(stmt.text, None))

        return stmt

    def cut(self, text, HMM=True):
        results = pseg.cut(text, HMM=HMM)
        seg, pos = [], []
        for s,p in results:
            seg.append(s)
            pos.append(p)

        return seg, pos

    def dependency_parse(self, text):
        # 调用pyltp进行依存句法分析
        return None

    def emotion_analysis(self, text, contexts):
        # 返回情感分析结果
        return None

if __name__ == "__main__":
    from Chatbot.sessions.statement import Statement

    p = Preprocessor(None)

    stmt = p.process(Statement(u"这是一个测试句子。"))

    print(stmt.get_segment())
    print(stmt.get_pos())
    print(stmt.get_emotion())