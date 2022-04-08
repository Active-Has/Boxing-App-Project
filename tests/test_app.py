from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Boxing_TMT


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()

        db.session.add(Boxing_TMT(club_name='Money TMT', address='24 Florida St', licence='yes'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestView(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_boxing(self):
        response = self.client.get(url_for('add_boxing_club'))
        self.assertEqual(response.status_code, 200)

