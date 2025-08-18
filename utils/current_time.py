from datetime import datetime
import pytz

def current_time():
    tehran_tz = pytz.timezone('Asia/Tehran')
    tehran_time = datetime.now(tehran_tz)
    return tehran_time.strftime("%Y-%m-%d %H:%M:%S")
