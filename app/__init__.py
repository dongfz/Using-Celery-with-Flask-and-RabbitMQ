import threading

from flask import Flask, request


class FlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskApp, self).__init__(*args, **kwargs)
        self._activate_background_job()

    def _activate_background_job(self):
        print(self.app_context())
        def run_job():
            print('1231313')
            # while True:
            #     print('1231313')

        t = threading.Thread(target=run_job)
        t.start()


def create_app() -> Flask:
    flask_app = FlaskApp(__name__)
    return flask_app
