from sqlalchemy import MetaData, Table, String, Integer, Column, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
import data_aggregation

base = declarative_base()
class blog_data(base):
    __tablename__ = "blog_data"
    id = Column(Integer(), primary_key=True)
    url = Column(String(200), nullable=False)
    post_title = Column(String(200), nullable=False)
    content = Column(Text(), nullable=False)
    published = Column(Boolean(), default=False)

base.metadata.create_all(data_aggregation.engine)