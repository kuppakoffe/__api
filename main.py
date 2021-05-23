from Services.db import db
from Resources.API import app


db.create_all()

if __name__ == '__main__':
    app.run(debug=True)