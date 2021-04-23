from datetime import datetime, timedelta
import pytz

class TestSaveDateToday(object):
    def test_o(self):

        date_now = datetime.now(pytz.timezone('Europe/Moscow'))
        in_two = date_now
        date_time = str(datetime.strftime(in_two, '%d.%m.%Y %H:%M:%S'))
        print(date_time)
