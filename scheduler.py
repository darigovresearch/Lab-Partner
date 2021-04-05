from crontab import CronTab


def reset_all():
    """reset_all is code to remove all crontab commands"""
    cron = CronTab(user='pi')
    cron.remove_all()
    cron.write()


def every_minute():
    """every_minute is code to a take photo ever  minute"""
    reset_all()
    cron = CronTab(user='pi')
    job = cron.new(command='python3 /home/pi/Lab-Partner/image_tools.py')
    job.minute.every(1)
    cron.write()


def every_five_minutes():
    """every_five_minutes is code to take a photo every five minutes"""
    reset_all()
    cron = CronTab(user='pi')
    job = cron.new(command='python3 /home/pi/Lab-Partner/image_tools.py')
    job.minute.every(5)
    cron.write()


def every_ten_minutes():
    """every_ten_minutes is code to take a photo every ten minutes"""
    reset_all()
    cron = CronTab(user='pi')
    job = cron.new(command='python3 /home/pi/Lab-Partner/image_tools.py')
    job.minute.every(10)
    cron.write()


def every_fifteen_minutes():
    """every_fifteen_minutes is code to take a photo every fifteen minutes"""
    reset_all()
    cron = CronTab(user='pi')
    job = cron.new(command='python3 /home/pi/Lab-Partner/image_tools.py')
    job.minute.every(15)
    cron.write()


def every_thirty_minutes():
    """every_thirty_minutes is code to take a photo every thirty minutes"""
    reset_all()
    cron = CronTab(user='pi')
    job = cron.new(command='python3 /home/pi/Lab-Partner/image_tools.py')
    job.minute.every(30)
    cron.write()


def every_sixty_minutes():
    """every_sixty_minutes is code to take a photo every sixty minutes"""
    reset_all()
    cron = CronTab(user='pi')
    job = cron.new(command='python3 /home/pi/Lab-Partner/image_tools.py')
    job.hour.every(1)
    cron.write()


if __name__ == '__main__':
    every_minute()
    # every_five_minutes()
    # every_ten_minutes()
    # every_fifteen_minutes()
    # every_thirty_minutes()
    # every_sixty_minutes()
