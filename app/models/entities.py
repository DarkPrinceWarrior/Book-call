from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.db_setup import Base



class Role(Base):
    __tablename__ = 'role'
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(40), nullable=False, unique=True)

    users = relationship('Users', backref='role', lazy="joined",
                             cascade='all, delete')

    def dictionarize(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name
        }


class Users(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(255), nullable=False,unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_token = Column(String(255), nullable=False, unique=True)
    role_id = Column(Integer, ForeignKey('role.role_id'), nullable=False)

    def dictionarize(self):
        return {
            "user_id": self.user_id,
            "user_token": self.user_token,
            "role_id": self.role_id
        }
