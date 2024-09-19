from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

# Database setup
Base = declarative_base()
db_url = "sqlite:///student_enrollment.db"
engine = create_engine(db_url, echo=True)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    enrollments = relationship("Enrollment", back_populates="student")


class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    courses = relationship("Course", back_populates="instructor")


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    instructor_id = Column(Integer, ForeignKey('instructors.id'), nullable=False)
    instructor = relationship("Instructor", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = 'enrollments'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


Base.metadata.create_all(engine)
