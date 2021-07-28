from datetime import datetime

sleep_t = datetime(2021, 7, 26, 22, 0, 0)
wakeup_t = datetime(2021, 7, 27, 6, 30, 0)

delta = wakeup_t - sleep_t
print(type(delta))
sec = delta.seconds
hours = sec / (60 * 60)
print('あと'+str(hours)+'時間です')