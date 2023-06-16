SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/test'



# imports = ('apps.tasks.tasks',)
# enable_utc = True
# timezone = 'Asia/Shanghai'
# broker_url = 'amqp://rabbit:123456@localhost:5672/test'
# result_backend = 'rpc://'
# beat_schedule = {
#     "test_sched_task": {
#         "task": "apps.tasks.tasks.test_sched_task",
#         "schedule": crontab(minute="*/1"),
#         "args": (1,)
#     },
# }