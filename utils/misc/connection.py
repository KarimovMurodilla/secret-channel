from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import update, delete
from sqlalchemy.orm import sessionmaker

from utils.db_api.base import Base
from utils.db_api.models import Users

db_string = r"sqlite:///database.db"
db = create_engine(db_string)  

Session = sessionmaker(db)  
session = Session()

Base.metadata.create_all(db)


class Database:
    # ---Users---
    def reg_user(self, user_id: str, username: str, name: str, insta: str, contact: str):
        """Some docs"""
        session.merge(Users(user_id = user_id, 
                            username = username,
                            name = name,
                            insta = insta,
                            contact = contact
                            )
                        )
        session.commit()