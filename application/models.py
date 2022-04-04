from application import db

class Boxing_TMT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(10))
    address = db.Column(db.varchar(30))
    licence = db.Column(db.BooleanField())
    boxer_id = db.Column('boxer_id', db.Integer, db.ForeignKey('boxer'))
    coach_id = db.Column('coach_id', db.Integer, db.ForeignKey('coach'))

class Boxer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    weight_class = db.Column(db.String(7))
    stance = db.Column(db.string(10))
    fighting_licence = db.Column(db.BooleanField())
    boxertmt = db.relationship('Boxing_TMT', backref='boxer')

class Coach(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    coach_type = db.Column(db.String(10))
    boxertmt = db.relationship('Boxing_TMT', backref='coach')


