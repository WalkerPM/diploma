import models
import data_aggregation
from sqlalchemy.orm import Session, sessionmaker
from distutils.util import strtobool
import csv

Session = sessionmaker(bind=data_aggregation.engine)

session = Session()

with open('import.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        entry = models.blog_data(
        url=row[0],
        post_title=row[1],
        content=row[2],
        published=strtobool(row[3]))  
        session.add(entry)
    session.commit()
