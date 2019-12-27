import time
from datetime import datetime
from playsound import playsound
class alarm_date():
    def __init__(self):
        pass

    def alarm(self,alarmtime):
        while True:
            if alarmtime[0]==time.localtime().tm_mday and alarmtime[1]==time.localtime().tm_hour and alarmtime[2]==time.localtime().tm_min:
                print("Wake Up!")
                playsound('/Users/soumyabratadutta/Downloads/ghungroo.mp3')
                break

i_alarm_date=alarm_date()
l1=[]
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
while len(l1)<3:
    l1.append(int(input(" Day: Hour : Minutes  :")))
i_alarm_date.alarm(l1)

#print (l1)