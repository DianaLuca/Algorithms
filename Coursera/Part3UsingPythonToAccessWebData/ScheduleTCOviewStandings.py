import schedule
import time

def job():
    print("Hello World! ...")

schedule.every(5).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)