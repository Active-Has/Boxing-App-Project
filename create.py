from application import db
from application.models import Boxing_TMT, Boxer

db.drop_all()
db.create_all()

# tmt1 = Boxing_TMT(club_name='Boxing TMT', address='24 Florida St', licence='yes')
# db.session.add(tmt1)
# db.session.commit()

# bx1 = Boxer(first_name='May', last_name='Weather', weight_class='lightweight', stance='orthodox', fighting_license='yes', boxingBr=tmt1)
# db.session.add(bx1)
# db.session.commit()

# bx2 = Boxer(first_name='Roy', last_name='Jones', weight_class='heavyweight', stance='southpaw', fighting_license='yes', boxingBr=tmt1)
# db.session.add(bx2)
# db.session.commit()


