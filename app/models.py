from app import db


class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dates = db.relationship("Dates", backref="event", lazy=True)

    def __repr__(self):
        return f"Events {self.id}: {self.name}"


votes_table = db.Table('votes_table',
                        db.Column('date_id', db.Integer, db.ForeignKey('dates.id')),
                        db.Column('person_id', db.Integer, db.ForeignKey('people.id')))

class Dates(db.Model):
    __tablename__ = "dates"
    id = db.Column(db.Integer, primary_key=True)
    date_format = db.Column(db.String(15), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    people = db.relationship("People", secondary=votes_table, backref=db.backref('votes', lazy='dynamic'))
    

    def __repr__(self):
        return f"Date {self.id}: {self.date_format}"


class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    

    def __repr__(self):
        return f"People {self.id}: {self.name}"