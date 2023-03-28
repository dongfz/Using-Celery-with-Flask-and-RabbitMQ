
from __future__ import absolute_import

from app.celery_tasks.main import celery_app


@celery_app.task
def test2(tesat: str):
    print(tesat)
    print('1231313')

