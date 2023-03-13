from __future__ import absolute_import
from celery import Celery

celery_app = Celery('demo', include=['celery_tasks'])  # 实例化celery对象
celery_app.config_from_object('celery_tasks.celeryconfig')  # 引入配置文件

if __name__ == '__main__':
    celery_app.start()
