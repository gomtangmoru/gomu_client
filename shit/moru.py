import logging
import tkinter as tk
import tkinter.messagebox as messagebox
from shit.jjampu import jjampu
from shit.use_potato import potato
from shit.wireguard import wireguard


class Moru:
    def __init__(self, root):
        self.root = root
        self.root.title("고무 스토리지")
        self.initlize()

    def initlize(self):
        if potato.use() is None:
            messagebox.showerror("저희도 바빠요", "서버로 부터 연락을 받을 수 없습니다, 서버가 바쁜가봅니다!");exit()
        if jjampu.give_me_token() != None: # 로컬에 토큰이 존재하는지 확인
            logging.info("로컬에 저장된 토큰을 발견하였습니다!")
            user_name = potato.vertify_token(jjampu.give_me_token())
            if user_name != False:
                logging.info("검증에 성공하였습니다 사용자명 : %s", user_name )
            else: logging.error("로컬에 있던 토큰으로 검증을 시도했지만 유효하지 않습니다.") # 토큰이 유효한지 검증, 파이썬 삼항 연산자가 왜 이렇게 생겼냐 ;;
        if wireguard.is_wiregurad() == False : logging.info("Wireguard가 존재하지 않아 설치 과정으로 건너뜁니다.");self.wireguard_installation()
        else:
            logging.info("로컬에서 토큰을 발견하지 못했습니다.");self.login_form()

    def controlpannel(self):
        pass


    def login_form(self):
        logging.info("로그인 체계를 불러옵니다.")
        self.label = tk.Label(self.root, text="로그인 정보를 입력하세요.")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.login_button = tk.Button(
            self.root,
            text="로그인",
            command=self.login_button_click
        )
        self.login_button.pack()


    def login_button_click(self):
        logging.debug("로그인 시도중")
        entry = str(self.entry.get())
        data = self.login(entry)
        if data == None:
            messagebox.showerror("오류", "연결이 유효하지 않거나 서버가 바쁩니다")
        messagebox.showinfo("정보", data)

    def wireguard_installation(self):
            messagebox.showerror("감자", "Wireguard가 설치되지 않았습니다. 설치 후 다시 시도 하십시오.")
            wireguard.wireguard_installer()
            exit()


    def login(self, token):
        data = potato.vertify_token(token)
        return data


