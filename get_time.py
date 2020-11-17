import datetime


class GetTime:

    def __init__(self):
        self.time_now = datetime.datetime.now()
        self.date_now = datetime.datetime.now().date()

    def get_current_time(self):
        # current time in format HH:MM
        current_time = datetime.timedelta(
            hours=self.time_now.hour,
            minutes=self.time_now.minute,
        )
        return current_time

    def get_current_date(self):
        # current date in format YYYY/MM/DD
        current_date = datetime.date(
            year=self.date_now.year,
            month=self.date_now.month,
            day=self.date_now.day,
        )
        return current_date

    @staticmethod
    def get_event_time(event):
        """ Getting event date in format YYYY/MM/DD and time in format HH:MM """

        raw_data = event['time'].split(" ")
        splitted_date = raw_data[0].split("-")

        event_date = datetime.date(
            int(splitted_date[0]),
            int(splitted_date[1]),
            int(splitted_date[2]),
        )

        splitted_time = raw_data[1].split(":")

        event_time = datetime.timedelta(
            hours=int(splitted_time[0]),
            minutes=int(splitted_time[1]),
        )

        return event_date, event_time
