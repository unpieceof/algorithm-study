# 10699. 오늘 날짜
from datetime import datetime, timedelta, timezone
datetime_utc = datetime.utcnow()

timezone_kst = timezone(timedelta(hours=9))
datetime_kst = datetime_utc.astimezone(timezone_kst)

print(datetime_kst.strftime("%Y-%m-%d"))