from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def start_scheduler(job):

    scheduler.add_job(
        job,
        "interval",
        minutes=1
    )

    scheduler.start()