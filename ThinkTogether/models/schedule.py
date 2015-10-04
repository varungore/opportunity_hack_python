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

# Define a Schedule model
class Schedule(Base):
    __tablename__ = 'schedule'

    # Location ID for the class
    siteID = db.Column(db.String(128), nullable=False, unique=True)

    # Curriculum ID
    currID = db.Column(db.String(128), nullable=False, unique=True)

    # Program Leader ID
    plID = db.Column(db.String(128), nullable=False, unique=True)

    # Start Date of a curriculum
    startDate = db.ColumnDefault(db.Date, nullable=False);

    # Start Time of the
# startDateTime
# classTime