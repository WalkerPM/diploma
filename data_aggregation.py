from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import sys

engine = create_engine(r'mariadb+mariadbconnector://api_user:Passw0rd@192.168.15.88:3306/migration')

import models

Session = sessionmaker(bind=engine)

engine.connect()
# try:
    
# except:
#     print("Connection to DB failed")
#     sys.exit(10)


def get_data(url):
    session = Session()
    output = session.query(models.blog_data).filter(models.blog_data.url == url).first()
    session.close()
    return output