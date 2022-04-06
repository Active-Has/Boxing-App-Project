from application import app, db
from application.models import Boxing_TMT, Boxer, BoxingtmtForm, BoxerForm
from flask import render_template, redirect, url_for, request
from application import models

@app.route('/')
def home():
    all_clubs = Boxing_TMT.query.all()
    return render_template('home.html', all_clubs=all_clubs)

@app.route('/add_club', methods=['GET', 'POST'])
def add_boxing_club():
    form = BoxingtmtForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            club = models.Boxing_TMT(club_name=form.club_name.data, address=form.address.data, licence=form.licence.data)
        db.session.add(club)
        db.session.commit()
        return redirect(url_for('home', message='Boxing Club Added'))
    else:
        return render_template('add_club.html', form=form)

@app.route('/add_boxer', methods=['GET', 'POST'])
def add_boxer():
    form = BoxerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            boxer = models.Boxer(first_name=form.first_name.data, last_name=form.last_name.data, weight_class=form.weight_class.data, stance=form.stance.data, fighting_licence=form.fighting_licence.data)
        db.session.add(boxer)
        db.session.commit()
        return redirect(url_for('home.html', message='Boxer Added'))
    else:
        return render_template('add_boxer.html', form=form)

@app.route('/view_boxers', methods=['GET', 'POST'])
def view_boxers():
    all_boxers = Boxer.query.all()
    return render_template('view_boxers.html', all_boxers=all_boxers)