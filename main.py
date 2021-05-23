from App.App import app
from services.Videos.Models.Videos import db
import resources.api


def main():
    db.create_all()
    app.run(debug=True)
