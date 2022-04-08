from application import app, db
from application.models import Boxing_TMT, Boxer, BoxingtmtForm, BoxerForm, AddClubForm
from flask import render_template, redirect, url_for, request

@app.route('/')
def home():
    all_clubs = Boxing_TMT.query.all()
    return render_template('home.html', all_clubs=all_clubs)


@app.route('/add_club', methods=['GET', 'POST'])
def add_boxing_club():
    form = BoxingtmtForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            club = Boxing_TMT(club_name=form.club_name.data, address=form.address.data, licence=form.licence.data)
            db.session.add(club)
            db.session.commit()
            return redirect(url_for('home', message='Boxing Club Added'))
        else:
            return render_template('add_club.html', form=form, message='Error')
    else:
        return render_template('add_club.html', form=form)


@app.route('/add_boxer', methods=['GET', 'POST'])
def add_boxer():
    form = BoxerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            boxer = Boxer(first_name=form.first_name.data, last_name=form.last_name.data, weight_class=form.weight_class.data, stance=form.stance.data, fighting_licence=form.fighting_licence.data, boxing_club=form.club_name.data)
            db.session.add(boxer)
            db.session.commit()
            return redirect(url_for('view_boxers', message='Boxer Added'))
        else:
            return render_template('add_boxer.html', form=form, message='Error')
    else:
        return render_template('add_boxer.html', form=form)

@app.route('/view_boxer', methods=['GET', 'POST'])
def view_boxers():
    all_boxers = Boxer.query.all()
    return render_template('view_boxer.html', all_boxers=all_boxers)



@app.route('/edit_1_club/<club_name>', methods=['GET', 'POST'])
def edit_club(club_name):
    form = BoxingtmtForm()
    edit_1_club = Boxing_TMT.query.filter_by(club_name=club_name).first()
    if request.method == 'POST':
        if edit_1_club:
            edit_1_club.club_name = form.club_name.data
            edit_1_club.address = form.address.data
            edit_1_club.licence = form.licence.data
            db.session.commit()
            return redirect(url_for('home', message='Club Edited'))
        else:
            return redirect(url_for('edit_club.html', message='Club Not Edited'))
    else:
        return render_template('edit_1_club.html', form=form, edit_1_club=edit_1_club)

@app.route('/edit_club', methods=['GET', 'POST'])
def edit():
    all_clubs = Boxing_TMT.query.all()
    return render_template('edit_club.html', all_clubs=all_clubs)


@app.route('/edit_1_boxer/<first_name>', methods=['GET', 'POST'])
def edit_boxer(first_name):
    form = BoxerForm()
    edit_1_boxer = Boxer.query.filter_by(first_name=first_name).first()
    if request.method == 'POST':
        if edit_1_boxer:
            edit_1_boxer.first_name = form.first_name.data
            edit_1_boxer.last_name = form.last_name.data
            edit_1_boxer.weight_class = form.weight_class.data
            edit_1_boxer.stance = form.stance.data
            edit_1_boxer.fighting_licence = form.fighting_licence.data
            edit_1_boxer.boxing_club = form.club_name.data
            db.session.commit()
            return redirect(url_for('view_boxers', message='Boxer Edited'))
        else:
            return redirect(url_for('edit_boxer.html', message='Boxer Not Edited'))
    else:
        return render_template('edit_1_boxer.html', form=form, edit_1_boxer=edit_1_boxer)

@app.route('/edit_boxer', methods=['GET', 'POST'])
def edit_boxer_view():
    all_boxers = Boxer.query.all()
    return render_template('edit_boxer.html', all_boxers=all_boxers)



@app.route('/delete_club/<club_name>', methods=['GET', 'POST'])
def delete_club(club_name):
    DClub = Boxing_TMT.query.filter_by(club_name=club_name).first()
    if DClub:
        db.session.delete(DClub)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_club.html', club_name=club_name)

@app.route('/delete_boxer/<first_name>', methods=['GET', 'POST'])
def delete_boxer(first_name):
    DBoxer = Boxer.query.filter_by(first_name=first_name).first()
    if DBoxer:
        db.session.delete(DBoxer)
        db.session.commit()
        return redirect(url_for('view_boxers'))
    return render_template('edit_boxer.html', first_name=first_name)