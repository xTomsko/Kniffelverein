from app.extensions import db


class Sheet(db.Model):
    __tablename__ = 'sheet'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    games = db.relationship("Game", backref="sheet")


class Game(Base):
    __tablename__ = 'game'

    id = db.Column(db.Integer, primary_key=True)
    sheet_id = db.Column(db.ForeignKey("sheet"))
    round = db.Column(db.SmallInteger)
    aces = db.Column(db.Integer)
    tows = db.Column(db.Integer)
    threes = db.Column(db.Integer)
    fours = db.Column(db.Integer)
    fives = db.Column(db.Integer)
    sixes = db.Column(db.Integer)
    bonus = db.Column(db.Boolean)
    upper_total = db.Column(db.Integer)
    triple = db.Column(db.Integer)
    quadruple = db.Column(db.Integer)
    full_house = db.Column(db.Integer)
    small_straight = db.Column(db.Integer)
    long_straight = db.Column(db.Integer)
    yahtzee = db.Column(db.Integer)
    chance = db.Column(db.Integer)
    lower_total = db.Column(db.Integer)
    total = db.Column(db.Integer)
