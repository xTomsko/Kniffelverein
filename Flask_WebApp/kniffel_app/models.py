from sqlalchemy import Column, Integer, SmallInteger, Boolean, Date, ForeignKey
from webapp.db import Base
from sqlalchemy.orm import relationship

class Sheet(Base):
    __tablename__ = 'sheet'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    games = relationship("Game", backref="sheet")

class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    sheet_id = Column(ForeignKey("sheet"))
    round = Column(SmallInteger)
    aces = Column(Integer)
    tows = Column(Integer)
    threes = Column(Integer)
    fours = Column(Integer)
    fives = Column(Integer)
    sixes = Column(Integer)
    bonus = Column(Boolean)
    upper_total = Column(Integer)
    triple = Column(Integer)
    quadruple = Column(Integer)
    full_house = Column(Integer)
    small_straight = Column(Integer)
    long_straight = Column(Integer)
    yahtzee = Column(Integer)
    chance = Column(Integer)
    lower_total = Column(Integer)
    total = Column(Integer)






