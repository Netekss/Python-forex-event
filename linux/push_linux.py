import notify2


def push(title, message):
    notify2.init('FX-event')
    notify = notify2.Notification(title, message)
    notify.show()
