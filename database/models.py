from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.ext.declarative import declarative_base
from config import async_session, engine

Base = declarative_base()

class Animals(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Integer)
    resource_prod_perHour = Column(Integer)

class ResourceTypes(Base):
    __tablename__ = "resource_types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    
class UserResources(Base):
    __tablename__ = "user_resources"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    resource_id = Column(Integer, ForeignKey("resource_types.id"))
    amount = Column(Integer)
    user = relationship("Users", backref="user_resources")
    resource = relationship("ResourceTypes", backref="user_resources")

    def __repr__(self):
        return f"UserResource(id={self.id!r}, user_id={self.user_id!r}, resource_id={self.resource_id!r}, amount={self.amount!r}, last_update={self.last_update!r})"
class UserAnimals(Base):
    __tablename__ = "user_animals"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    animal_id = Column(Integer, ForeignKey("animals.id"))
    amount = Column(Integer)
    user = relationship("Users", backref="user_animals")
    animal = relationship("Animals", backref="user_animals")
    def __repr__(self):
        return f"UserAnimal(id={self.id!r}, user_id={self.user_id!r}, animal_id={self.animal_id!r}, amount={self.amount!r}, last_update={self.last_update!r})"

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    def __repr__(self):
        return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"
    
    def __str__(self):
        return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"

    async def save(self):
        async with async_session as session:
            session.add(self)
            await session.commit()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
