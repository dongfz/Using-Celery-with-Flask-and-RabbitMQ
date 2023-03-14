import time

if __name__ == '__main__':
    from celery_tasks.tasks import test2
    test2.delay('123131')

    time.sleep(100)