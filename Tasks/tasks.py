from Tasks.flask_celery import make_celery
from App.App import app


tasks = make_celery(app)