from sqlalchemy import Integer, Column
from sqlalchemy.orm import DeclarativeBase, MappedColumn


class Base(DeclarativeBase):
    pass

class TableThread(Base):
    __tablename__ = "TableThread"
    id = Column(Integer, primary_key=True)
    count=Column(Integer(), default=0)
