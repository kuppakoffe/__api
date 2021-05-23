from Services.db import db
from Resources.API import app

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)