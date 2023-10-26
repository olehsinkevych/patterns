from sqlalchemy import Column, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import List

from app.db.database import Base

'''
class Container(Base):
    __tablename__ = "containers"


class Item(Base):
    __tablename__ = "items"
'''


class Port(Base):
    __tablename__ = "ports"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    ships: Mapped[List["Ship"]] = relationship(back_populates="port")


class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[int] = mapped_column(primary_key=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    type = Column(String(15), nullable=False, unique=False, index=True)
    fuel = Column(Float, nullable=False, unique=False)
    port_id: Mapped[int] = mapped_column(ForeignKey("ports.id"))
    port: Mapped["Port"] = relationship(back_populates="ships")

    def __repr__(self):
        return f'Ship(title={self.title})'
