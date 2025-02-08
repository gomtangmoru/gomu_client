import logging, os, ctypes, sys, subprocess
import tkinter as tk
from shit.jjampu import jjampu
from shit.moru import Moru
from shit.use_potato import potato
from shit.wireguard import wireguard

# 파이썬 배우지 말고 golang이나 배울껄


def ass():
    try:
        ctypes.windll.kernel32.AllocConsole()
        sys.stdout = open('CONOUT$', 'w')
        sys.stderr = open('CONOUT$', 'w')
        root_logger = logging.getLogger()
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
        root_logger.setLevel(logging.DEBUG)
        logging.info("로깅 헨들러가 성공적으로 초기화하였습니다")
    except Exception as e:
        print(f"초기화에 오류가 발생했습니다: {e}")




def main():
    if jjampu.is_appdata_shit() == False:
        jjampu.make_shit_in_appdata()
    if jjampu.i_want_shit() == True:
        ass()
        logging.info("디버그 시작")
    root = tk.Tk()
    app = Moru(root)
    root.mainloop()



if __name__ == "__main__":
    main()


    

