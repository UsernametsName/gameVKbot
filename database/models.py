from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.ext.declarative import declarative_base
from config import async_session, engine

Base = declarative_base()

class Animals(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    resource_prod_perHour = Column(Integer)

class Resources(Base):
    __tablename__ = "resources"
    id = Column(Integer, ForeignKey('users.id'), primary_key=True) 
    coins = Column(Integer)
    eggs = Column(Integer)
    milk = Column(Integer)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    resources = relationship("Resources", backref="user")
    
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
