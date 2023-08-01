from models import Dog
from sqlalchemy import create_engine


def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    names = session.query(Dog).all()
    return names

def find_by_name(session, name):
    name = session.query(Dog).filter_by(name=name).first()
    return name

def find_by_id(session, id):
    name = session.query(Dog).filter_by(id=id).first()
    return name

def find_by_name_and_breed(session, name, breed):
    name = session.query(Dog).filter_by(name=name, breed=breed).first()
    return name

def update_breed(session, dog, breed):
    session.query(Dog).filter_by(name=dog.name).update({'breed': breed})