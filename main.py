import time
import datetime
from push import Push
from get_time import GetTime
from get_data import get_events

events = get_events()
incoming_events = []

def run_main(events):
    while True:
        current_time = GetTime().get_current_time()

        for event in events:
            if (event['time'] > current_time) and (event['time'] < (current_time + datetime.timedelta(hours=1))):
                incoming_events.append(event)

        if len(incoming_events) == 0:
            push = Push(str(current_time), 'No incoming events within an hour')
            push.auto_select_os()
        else:
            for incoming_event in incoming_events:
                push = Push(f"Incoming event at {str(incoming_event['time'])}", incoming_event['name'])
                push.auto_select_os()

        incoming_events.clear()
        time.sleep(3200)


run_main(events)
