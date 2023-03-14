from kombu import Queue

broker_url = 'amqp://rabbit:123456@192.168.3.243:5672//'
celery_result_backend = 'amqp://rabbit:123456@192.168.3.243:5672//'
task_queues = (
    Queue('task-test2', routing_key='route.task-test2'),
)

task_routes = {
    'demo.tasks.test2': {
        'queue': 'task-test2',
        'routing_key': 'route.task-test2',
    }
}

