from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Boxing_TMT, Boxer, BoxerForm, BoxingtmtForm
from flask import url_for
from flask_testing import TestCase


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()
        
        tmt1 = Boxing_TMT(club_name='Boxing TMT', address='24 Florida St', licence='yes')
        tmt2 = Boxing_TMT(club_name='The Money Team', address='Victoria Road London', licence='yes')
        
        bx1 = Boxer(first_name='May Weather', last_name='Junior', weight_class='lightweight', stance='orthodox', fighting_licence='yes', boxingBr=tmt1)
        bx2 = Boxer(first_name='Roy', last_name='Jones', weight_class='heavyweight', stance='southpaw', fighting_licence='yes', boxingBr=tmt1)
        bx3 = Boxer(first_name='John', last_name='Doe', weight_class='middleweight', stance='southpaw', fighting_licence='no', boxingBr=tmt2)
        
        db.session.add_all([tmt1, tmt2, bx1, bx2, bx3])
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
    
    def test_add_boxer(self):
        response = self.client.get(url_for('add_boxer'))
        self.assertEqual(response.status_code, 200)

    def view_boxer(self):
        response = self.client.get(url_for('view_boxer'))
        self.assertEqual(response.status_code, 200)
    
    def edit_boxing(self):
        response = self.client.get(url_for('edit_boxing'))
        self.assertEqual(response.status_code, 200)
    
    def edit_boxer(self):
        response = self.client.get(url_for('edit_boxer'))
        self.assertEqual(response.status_code, 200)


class TestView1(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        assert "Welcome to the Boxing App" in response.data.decode()

    def test_view_boxer(self):
        response = self.client.get(url_for('view_boxers'))
        assert 'Roy' in response.data.decode()
        assert 'Junior' in response.data.decode()
        assert 'middleweight' in response.data.decode()
        assert 'southpaw' in response.data.decode()
        assert 'no' in response.data.decode()
    
    def test_view_boxing(self):
        response = self.client.get(url_for('home'))
        assert 'Boxing TMT' in response.data.decode()
        assert 'Victoria Road London' in response.data.decode()
        assert 'yes' in response.data.decode()


class TestCreate(TestBase):

    def test_create_boxing(self):
        response = self.client.post(url_for('add_boxing_club'), data=dict(
            club_name='Boxing TMT', address='24 Florida St', licence='yes'), 
            follow_redirects=True)
        assert 'Boxing TMT' in response.data.decode()
        assert '24 Florida St' in response.data.decode()
        assert 'yes' in response.data.decode()

    def test_create_boxer(self):
        response = self.client.post(url_for('add_boxer'), data=dict(
            first_name='May Weather', last_name='Junior', weight_class='lightweight', stance='orthodox', fighting_licence='yes', boxingBr=1), 
            follow_redirects=True)
        assert 'May Weather' in response.data.decode()
        assert 'Junior' in response.data.decode()
        assert 'light weight' in response.data.decode()
        assert 'orthodox' in response.data.decode()
        assert 'yes' in response.data.decode()
        assert '1' in response.data.decode()


class TestEdit(TestBase):

    def test_edit_boxing(self):
        response = self.client.post(url_for('edit_club', club_name='Boxing TMT'), data=dict(
            club_name='Boxing TMT', address='24 Florida St', licence='yes'), 
            follow_redirects=True)
        assert 'Boxing TMT' in response.data.decode()
        assert '24 Florida St' in response.data.decode()
        assert 'yes' in response.data.decode()

    def test_edit_boxer(self):
        response = self.client.post(url_for('edit_boxer', first_name='May Weather'), data=dict(
            first_name='May Weather', last_name='Junior', weight_class='lightweight', stance='orthodox', fighting_licence='yes', boxingBr=1), 
            follow_redirects=True)
        assert "/" in response.data.decode()


class TestDelete(TestBase):

    def test_delete_boxing(self):
        response1 = self.client.get(url_for('delete_boxer', first_name='May Weather'), follow_redirects=True)
        response = self.client.get(url_for('delete_club', club_name='Boxing TMT'), follow_redirects=True)
        assert 'View Boxers' in response1.data.decode()
        assert '/' in response.data.decode()

    def test_delete_boxer(self):
        response = self.client.get(url_for('delete_boxer', first_name='May Weather'), follow_redirects=True)
        assert 'View Boxers' in response.data.decode()