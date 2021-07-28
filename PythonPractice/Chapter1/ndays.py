from datetime import datetime, timedelta

base_t = datetime(2021, 7, 26)
t = base_t + timedelta(days=7)
print(t.strftime('%Y/%m/%d'))