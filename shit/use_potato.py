# 서버 통신단
import requests, logging, json

class potato:
    def __init__(self):
        self.server_url = ""

    def use(self):
        target = self.server_url+"live"
        logging.info("목적 URL : %s", str(target))
        try:
            data = requests.get(target)
            logging.info("인증 서버로부터 연락을 받았습니다.")
        except requests.exceptions.RequestException as e:
            logging.error("서버가 바쁩니다.\n", e)
            return None
        return True

    def vertify_token(self, token: str):
        value = {"token" : f"{token}"}
        try:
            req = requests.post(self.server_url+"login", json=value)
            data = req.json()
        except requests.exceptions.RequestException as e:
            return False
        if data['status']:return data['name']
        return False


potato = potato()