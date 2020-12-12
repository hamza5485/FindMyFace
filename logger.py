import datetime


class Logger:
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    WHITE = '\033[0;37m'
    END = '\033[1;37;0m'

    def info(self, message):
        print(f"{self.WHITE}[{datetime.date.today().isoformat()}][INFO]: {message}{self.END}")

    def success(self, message):
        print(f"{self.GREEN}[{datetime.date.today().isoformat()}][SUCCESS]: {message}{self.END}")

    def error(self, message):
        print(f"{self.RED}[{datetime.date.today().isoformat()}][ERROR]: {message}{self.END}")

    def warn(self, message):
        print(f"{self.YELLOW}[{datetime.date.today().isoformat()}][WARN]: {message}{self.END}")
