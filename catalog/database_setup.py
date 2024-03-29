from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


@property
def serialize(self):
    """Return object data in easily serializeable format"""
    return {'name': self.name, 'id': self.id}


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    picture = Column(String(250))
    variety = Column(String(250))
    package_id = Column(Integer, ForeignKey('package.id'))
    package = relationship(Package, backref=backref(
                     'menu_item', cascade='all,delete'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


@property
def serialize(self):
    """Return object data in easily serializeable format"""
    return {'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'picture': self.picture,
            'variety': self.variety}


engine = create_engine('sqlite:///packagedata.db')


Base.metadata.create_all(engine)
