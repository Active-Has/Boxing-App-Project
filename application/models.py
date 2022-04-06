from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

class Boxing_TMT(db.Model):
    __tablename__ = 'boxingtmt'
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    licence = db.Column(db.String(3), nullable=False)
    boxerID = db.relationship('Boxer', backref='boxingBr')

class Boxer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    weight_class = db.Column(db.String(15), nullable=False)
    stance = db.Column(db.String(10), nullable=False)
    fighting_licence = db.Column(db.String(3), nullable=False)
    boxing_club = db.Column(db.Integer, db.ForeignKey('boxingtmt.id'), nullable=False)

# class Coach(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(10), nullable=False)
#     last_name = db.Column(db.String(10), nullable=False)
#     coach_type = db.Column(db.String(10), nullable=False)
#     boxertmt = db.relationship('Boxing_TMT', backref='coach')

# class AddCoachForm(FlaskForm):
#     first_name = StringField('First name', validators=[DataRequired()])
#     last_name = StringField('Last name', validators=[DataRequired()])
#     coach_type = SelectField('Type', choices=[('pad_work', 'Pad Work'), ('punch_bag', 'Punch Bag'), ('fitness', 'Fitness')])

# def boxer_query():
#     return Boxer.query
# def coach_query():
#     return Coach.query

class BoxerForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    weight_class = SelectField('Weight Class', choices=[('feather_weight', 'Feather Weight'), 
                ('light_weight', 'Light Weight'), ('welter_weight', 'Welter Weight'),
                ('middle_weight', 'Middle Weight'), ('heavy_weight', 'Heavy Weight')
                ])
    stance = SelectField('Stance', choices=([('southpaw', 'Southpaw'), ('orthodox', 'Orthodox')]))
    fighting_licence = SelectField('Fighting Licence', choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Add Boxer')

class BoxingtmtForm(FlaskForm):
    club_name = StringField('Boxing Club Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    licence = SelectField('Licence', choices=[('yes','Yes'), ('no','No')])
    submit = SubmitField('Add Boxing Club')