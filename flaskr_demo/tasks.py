from celery import shared_task


@shared_task
def test2(tesat: str):
    print(tesat)
    print('1231313')


@shared_task
def test_sched_task(test: int):
    print("12313515test_sched_task")