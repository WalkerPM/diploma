from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import sys

engine = create_engine('sqlite:///sqlite3.db')

import models

Session = sessionmaker(bind=engine)


try:
    engine.connect()
except:
    print("Connection to DB failed")
    sys.exit(10)


def get_data(url):
    session = Session()
    output = session.query(models.blog_data).filter(models.blog_data.url == url).first()
    session.close()
    return output