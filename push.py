from sys import platform

try:
    from windows import push_win10
except:
    from linux import push_linux


class Push:

    def __init__(self, title, message):
        self.os = platform
        self.title = title
        self.message = message

    def auto_select_os(self):
        if self.os.startswith("win32"):
            push_win10.push(self.title, self.message)
        elif self.os.startswith("linux"):
            push_linux.push(self.title, self.message)
