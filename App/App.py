from flask import Flask

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/app'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.update(
    CELERY_BROKER_URL="redis://localhost:6379",
    CELERY_RESULT_BACKEND="redis://localhost:6379",
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@localhost:5432/app",
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)
