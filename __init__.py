from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
from quote_scrapper import scrap_quotes

class Quote(db.Model):
  __tablname__ = 'quotes'
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.Text())
  text = db.Column(db.Text())

  def __init__(self, author, text):
    self.author = author
    self.text = text

class Tag(db.Model):
  __tablname__ = 'tags'
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(200))
  quote_id = db.Column(db.Integer, db.ForeignKey('quote.id'))

  def __init__(self, text, quote_id):
    self.text = text
    self.quote_id = quote_id

@app.route('/')
def index():
  return 'Welcome to my web scrapper'

@app.route('/start', methods=['POST'])
def startScrapper():
  if request.method == 'POST':
    scrap_quotes()
    return 'Scrapper started!!'
  return 'Naaaaaaaaahh B.'
