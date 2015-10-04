__author__ = 'dhara'

# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from ThinkTogether import db


# Define a base model for other database tables to inherit
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Curriculum(Base):
    __tablename__ = 'curriculum'

    # Duration of the Curriculum
    days = db.Column(db.Integer, nullable=True, db.CheckConstraint('0 <= days <=31'))
    month = db.Column(db.Integer, nullable=True, db.CheckConstraint('0 <= month <=12'))
    year = db.Column(db.Integer, nullable=True)

    # Name and location of the Curriculum file
    fileName = db.Column(db.TEXT, nullable=True)
    fileLocation = db.Column(db.TEXT, nullable=False)

    # New instance
    def __init__(self, days, month, year, fileName, fileLocation):
        self.days = days
        self.month = month
        self.year = year
        self.fileName = fileName
        self.fileLocation = fileLocation

    def __repr__(self):
        return '<File %r>' % (self.name)
