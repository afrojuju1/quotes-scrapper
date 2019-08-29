from app import db

class Quote(db.Model):
  __tablname__ = 'quotes'
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.String(300))
  text = db.Column(db.String(1000))

  def __init__(self, author, text):
    self.author = author
    self.text = text
