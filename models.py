from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False)
    age = Column(Date, nullable=False)
    weight = Column(Integer, nullable=False)
    activity = Column(Integer, nullable=False)


class Complex(Base):
    __tablename__ = 'complex'

    complex_name = Column(String(20), primary_key=True)

class User_do_complex(Base):
    __tablename__ = 'user_do_complex'

    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    complex_name = Column(String(20), ForeignKey('complex.complex_name'), primary_key=True)
    time_start = Column(DateTime, primary_key=True)
    status = Column(String(20), nullable=False)

class Club(Base):
    __tablename__ = 'club'

    club_name = Column(String(20), primary_key=True)
    prise = Column(Integer, nullable=False)
    city = Column(String(6), nullable=False)
    rating = Column(Integer, nullable=False)

class Club_has_complex(Base):
    __tablename__ = 'club_do_complex'

    club_name = Column(String(20), ForeignKey('club.club_name'), primary_key=True)
    complex_name = Column(String(20), ForeignKey('complex.complex_name'), primary_key=True)
