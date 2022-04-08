from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField

class Boxing_TMT(db.Model):
    __tablename__ = 'boxingtmt'
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    licence = db.Column(db.String(3), nullable=False)
    boxerID = db.relationship('Boxer', backref='boxingBr')

    def __repr__(self):
        return 'Choose {}'.format(self.club_name)


class Boxer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    weight_class = db.Column(db.String(15), nullable=False)
    stance = db.Column(db.String(10), nullable=False)
    fighting_licence = db.Column(db.String(3), nullable=False)
    boxing_club = db.Column(db.String, db.ForeignKey('boxingtmt.id'), nullable=False)

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
    weight_class = SelectField('Weight Class', choices=[('feather weight', 'Feather Weight'), 
                ('light weight', 'Light Weight'), ('welter weight', 'Welter Weight'),
                ('middle weight', 'Middle Weight'), ('heavy weight', 'Heavy Weight')
                ])
    stance = SelectField('Stance', choices=([('southpaw', 'Southpaw'), ('orthodox', 'Orthodox')]))
    fighting_licence = SelectField('Fighting Licence', choices=[('yes', 'Yes'), ('no', 'No')])
    club_name = StringField('Boxing Club:', validators=[DataRequired()])
    submit = SubmitField('Add Boxer')

class BoxingtmtForm(FlaskForm):
    club_name = StringField('Boxing Club Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    licence = SelectField('Licence', choices=[('yes','Yes'), ('no','No')])
    submit = SubmitField('Add Boxing Club')

class AddClubForm(FlaskForm):
    club_name = SelectField('Boxing Club Name', choices=[])
    address = SelectField('Address', choices=[])
    licence = SelectField('Licence', choices=[('yes','Yes'), ('no','No')])
    submit = SubmitField('Confirm Edit')

class AddBoxerForm(FlaskForm):
    first_name = SelectField('First Name', choices=[])
    last_name = SelectField('Last Name', choices=[])
    weight_class = SelectField('Weight Class', choices=[('feather weight', 'Feather Weight'), 
                ('light weight', 'Light Weight'), ('welter weight', 'Welter Weight'),
                ('middle weight', 'Middle Weight'), ('heavy weight', 'Heavy Weight')
                ])
    stance = SelectField('Stance', choices=([('southpaw', 'Southpaw'), ('orthodox', 'Orthodox')]))
    fighting_licence = SelectField('Fighting Licence', choices=[('yes', 'Yes'), ('no', 'No')])
    club_name = SelectField('Boxing Club', choices=[])
    submit = SubmitField('Add Boxer')

