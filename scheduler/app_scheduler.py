import schedule
import time
from datetime import datetime, time as tm


def task():
    print(f"Task running... {datetime.now()}")


# schedule.every(3).seconds.do(task)
# schedule.every().day.at("15:41").do(task)
# schedule.every().hour.at(":42").do(task)
# schedule.every().second.until("15:44").do(task)
schedule.every().second.until(tm(15, 57, 5)).do(task)

while True:
    schedule.run_pending()
    time.sleep(1)