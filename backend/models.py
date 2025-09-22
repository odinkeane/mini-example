from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import Settings

engine = create_engine(Settings.get_database_url())
Session = sessionmaker(engine)
BaseModel = declarative_base()

class Student(BaseModel):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    secondname = Column(String)
    patronymic = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<Студент: {self.secondname} {self.firstname[0]}. {self.patronymic[0]}. />"


if __name__ == "__main__":
    BaseModel.metadata.create_all(engine)