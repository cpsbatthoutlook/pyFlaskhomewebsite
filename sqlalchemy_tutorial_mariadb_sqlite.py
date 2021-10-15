from flask import Flask
from flask_sqlalchemy import SQLAlchemy  ##mariadb module needed 

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///book.db'   #use Sqlite location for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://operator:tej1nder@192.168.0.172:3306/Server'
db = SQLAlchemy(app)


class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    catagory = db.Column(db.String(80), unique=True)
    details = db.Column(db.String(120), unique=True)
    url = db.Column(db.String(120), unique=True)
    inserttime = db.column(db.DateTime)
    def __init__(self, Bookmarksname, email):
        self.catagory = catagory
        self.details = details
    def __repr__(self):
        return '<Bookmarks %r>' % self.details

# admin = Bookmarks('admin', 'admin@example.com')
# db.create_all() # In case Bookmarks table doesn't exists already. Else remove it.    
# db.session.add(admin)
# db.session.commit() # This is needed to write the changes to database
Bookmarks.query.all()

#Paginate  https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/?highlight=paginate#flask_sqlalchemy.BaseQuery.paginate
xx=Bookmarks.query.paginate(per_page=30)
xx.per_page  ##per page
xx.page   ##Current
xx.pages ##Total pages
xx.total ##Total records
for x in xx.items: ##List items
    print(x)

for x in xx.iter_pages(): ## list pages
    print(x)

# Create Drop tables https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/
Bookmarks.create_all()
Bookmarks.drop_all()


#  SELECT WHERE  : https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
Bookmarks.query.filter_by(catagory='Apache').all()  ## first(), 
Bookmarks.query.get(1)  #by primary key
Bookmarks.query.limit(1).all()  ## limit
Bookmarks.query.order_by(User.username).all() # ORDER by
Bookmarks.query.filter(Bookmarks.catagory.endswith('e')).all() # like %e



