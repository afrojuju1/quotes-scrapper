from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/quotesscrapper'
app.debug = True

# from models.quote import Quote
# from models.tag import Tag
#
# db.create_all()
# db.session.commit()

"""
  steps to create db
  1. pipenv run python or python
  2. from app import db
  3. db.create_all()
  4. exit()
"""

@app.route('/')
def index():
  return 'Welcome to my web scrapper'

@app.route('/start', methods=['POST'])
def startScrapper():
  if request.method == 'POST':
    from quote_scrapper import scrap_quotes
    scrap_quotes()
    return 'Scrapper started!!'
  return 'Naaaaaaaaahh B.'

if __name__ == '__main__':
  app.run()