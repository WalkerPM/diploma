from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
import yaml
import sys

with open("./env.yaml") as file:
            evariables = yaml.safe_load(file)

engine = create_engine(r'mariadb+mariadbconnector://' + str(evariables['db']['user']) +':' + str(evariables['db']['pass']) + '@' + str(evariables['db']['ip']) + '/' + evariables['db']['db_name'])

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