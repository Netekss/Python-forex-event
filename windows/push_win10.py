from win10toast import ToastNotifier


def push(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, duration=5)
