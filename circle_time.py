import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
# from app.untils.log_builder import sys_logging

scheduler = BlockingScheduler()   # 后台运行

 # 设置为每日凌晨00:30:30时执行一次调度程序
@scheduler.scheduled_job("cron", day_of_week='*', hour='1', minute='30', second='30')
def rebate():
        print("schedule execute")
        # sys_logging.debug("statistic scheduler execute success" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    try:
        scheduler.start()
        # sys_logging.debug("statistic scheduler start success")
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        # sys_logging.debug("statistic scheduler start-up fail")