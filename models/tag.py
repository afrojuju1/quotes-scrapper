from app import db

class Tag(db.Model):
  __tablname__ = 'tags'
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(200))
  quote_id = db.Column(db.Integer, db.ForeignKey('quote.id'))

  def __init__(self, text, quote_id):
    self.text = text
    self.quote_id = quote_id
