from Tasks.flask_celery import make_celery
from App.App import app

celery = make_celery(app)
