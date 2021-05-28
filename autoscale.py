from apscheduler.schedulers.blocking import BlockingScheduler
from waxrix import checking_new_coin 
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def job():
    checking_new_coin()
    


sched.start()