from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Student, Session
from settings import Settings


class StudentService:



    @staticmethod
    def get_students():
        session = Session()
        result = session.query(Student).all()
        session.close()
        return result 
        
    @staticmethod
    def get_student_by_id(id):
        session = Session()
        student = session.query(Student).filter(Student.id == id).first()
        session.close()
        return student

    @staticmethod
    def add_student(firstname, secondname, patronymic, age):
        session = Session()
        student = Student(firstname=firstname, 
                          secondname=secondname, 
                          patronymic=patronymic, 
                          age=age
                          )
        session.add(student)
        session.commit()
        session.close()
