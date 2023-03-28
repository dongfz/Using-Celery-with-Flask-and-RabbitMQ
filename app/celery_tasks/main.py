from __future__ import absolute_import

import kombu
from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue

celery_app = Celery('demo', include=['celery_tasks'])
celery_app.config_from_object('celery_tasks.celeryconfig')

my_queue = Queue('custom', Exchange('custom'), 'routing_key')
my_queue2 = Queue('custom2', Exchange('custom'), 'routing_key2')


def _handle_message(body, message: kombu.Message):
    print('Received message: {0!r}'.format(body))
    message.ack()


class MyConsumerStep(bootsteps.ConsumerStep):
    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[my_queue, my_queue2],
                         callbacks=[_handle_message],
                         accept=['json'])]


celery_app.steps['consumer'].add(MyConsumerStep)

if __name__ == '__main__':
    celery_app.start()
