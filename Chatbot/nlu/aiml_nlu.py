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
        self.aiml.learn(configs.aiml_nlu_path)
        self.aiml.respond(configs.aiml_nlu_learn)

    def process(self, stmt):
        res = self.aiml.respond(stmt.text)

        if self.configs.debug_mode: print("[AimlNLU]:\'%s\'" % res)

        if "Greeting" in res:               # 问候
            return "Greeting", None
        elif "SEARCHBYSONG" in res:         # 按歌曲名搜索
            song = res.strip().split(":")[-1]
            return "SearchBySong", {"song": song}
        elif "SEARCHBYSINGER" in res:       # 按歌手搜索
            singer = res.strip().split(":")[-1]
            return "SearchBySinger", {"singer": singer}
        elif "SEARCHBYTYPE" in res:         # 按歌曲类型搜索
            type = res.strip().split(":")[-1]
            return "SearchByType", {"type": type}
        elif "SEARCHBYSCENE" in res:        # 按场景搜索
            scene = res.strip().split(":")[-1]
            return "SearchByScene", {"scene": scene}
        else:
            return None, None

if __name__ == "__main__":

    from Chatbot.configs import Configs
    from Chatbot.sessions.statement import Statement
    cfg = Configs()

    cfg.aiml_nlu_path = "../aiml/nlu-startup.xml"

    nlu = AimlNLU(cfg)
    nlu.process(Statement(text="搜 haoting 的歌"))
