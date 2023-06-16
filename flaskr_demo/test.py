

# def create_celery_app(flask_app: Flask) -> Celery:
#     class FlaskTask(Task, ABC):
#         def __call__(self, *args: object, **kwargs: object) -> object:
#             with flask_app.app_context():
#                 return self.run(*args, **kwargs)

#     celery_app = Celery(flask_app.name, task_cls=FlaskTask)
#     celery_app.config_from_object('DefaultConfig')
#     celery_app.set_default()
#     flask_app.extensions["CELERY_APP"] = celery_app
#     return celery_app


# class FlaskApp(Flask):
#     def __init__(self, *args, **kwargs):
#         super(FlaskApp, self).__init__(*args, **kwargs)
#         self._activate_background_job()

#     def _activate_background_job(self):
#         print(self.app_context())

#         def run_job():
#             print('_activate_background_job1231313')
#             with self.app_context():
#                 print('_activate_background_job12313')
#             # while True:
#             #     print('1231313')

#         t = threading.Thread(target=run_job)
#         t.start()
