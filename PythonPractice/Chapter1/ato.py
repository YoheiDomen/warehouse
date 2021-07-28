from datetime import datetime

yoteibi = datetime(2024, 2, 19)
now = datetime.now()
delta = yoteibi - now
print('あと'+str(delta.days+1) + '日です')