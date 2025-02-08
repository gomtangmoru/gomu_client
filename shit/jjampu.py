# 로컬 저장 파일 조회
import json
import logging
import os, requests

class jjampu:
    def __init__(self):
        self.APPDATA = os.path.join(os.getenv('APPDATA'), 'gomutree')
        logging.info("self.APPDATA = %s", self.APPDATA)

    def is_appdata_shit(self):
        return os.path.exists(self.APPDATA)
    
    def make_shit_in_appdata(self):
        os.makedirs(self.APPDATA)
        logging.info("기억 위치를 성공적으로 기록하였습니다. 기록 위치 : %s", self.APPDATA)
        
    def i_want_shit(self):
        return os.path.isfile(os.path.join(self.APPDATA, "DEBUG.txt"))


    def give_me_token(self):
        if os.path.isfile(os.path.join(self.APPDATA, "token.json")):
            with open(os.path.join(self.APPDATA, "token.json")) as f:
                return json.load(f)
        else:
            return None


    def write_token(self, token):
        with open(os.path.join(self.APPDATA, "token.json"), "w") as f:
            json.dump(token, f)

jjampu = jjampu()