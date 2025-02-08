import subprocess, logging

class shell:
    def run(self, command):
        logging.info("다음과 같은 명령을 전달받았습니다 %s", command)
        try:
            result = subprocess.run(command, shell=True, capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(e)
            return None
        return result


shell = shell()