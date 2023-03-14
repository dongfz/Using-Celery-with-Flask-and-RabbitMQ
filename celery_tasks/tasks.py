
from __future__ import absolute_import

from celery_tasks.main import celery_app


@celery_app.task
def test2(tesat: str):
    print(tesat)
    print('1231313')

