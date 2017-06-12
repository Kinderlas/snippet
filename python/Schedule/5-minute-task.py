import sched
import datetime
import time

schedule = sched.scheduler(time.time, time.sleep)

def start_schedule():
    start_time_str = "2017-06-12 15:50"
    t = time.strptime(start_time_str, "%Y-%m-%d %H:%M")
    # schedule.enterabs(start_time, priority, function, (augument))
    schedule.enterabs(time.mktime(t), 0, start_record_click, ())
    # schedule.enterabs(0, 0, start_record_click, ())
    schedule.run()

def start_record_click():
    # run every 5 minutes
    # schedule.enter(delay, priority, function, (augument))
    schedule.enter(5 * 60, 0, start_record_click, ())

def main():
    start_schedule()
