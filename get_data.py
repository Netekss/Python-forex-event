import requests
from get_time import GetTime

current_time = GetTime().get_current_time()
current_date = GetTime().get_current_date()


def get_events():
    # api config
    api = requests.get('https://finnhub.io/api/v1/calendar/economic?token=btu9bp748v6vqmm3eckg')
    calendar = api.json()

    # adding today events
    events_today = []
    filter_list = []  # for special key created from event hour and first word from event name

    for event in calendar['economicCalendar']:
        event_date = GetTime().get_event_time(event)[0]
        event_time = GetTime().get_event_time(event)[1]

        if event_date == current_date:
            event_name = event['event']

            new_event = {"date": event_date,
                         "time": event_time,
                         "name": event_name,
                         'filter': f'{str(event_time)}-{event_name.split(" ")[0]}',
                         }

            events_today.append(new_event)
            filter_list.append(new_event['filter'])

    # avoiding multiply notifications for events with the same currency and hour
    unique = set(filter_list)
    filtered_events = []
    check = []

    for event in events_today:
        for filter in unique:
            if (filter == event['filter']) and (filter not in check):
                check.append(filter)
                filtered_events.append(event)

    return filtered_events
