from datetime import datetime
from pytz import timezone

def get_datetime_now():
    bucharest = timezone('Europe/Bucharest')
    bucharest_time = datetime.now(bucharest)
    bucharest_strftime = bucharest_time.strftime('%Y-%m-%d %H:%M:%S')
    return datetime.strptime(bucharest_strftime, "%Y-%m-%d %H:%M:%S")
