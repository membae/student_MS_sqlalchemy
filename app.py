from sqlalchemy.orm import sessionmaker
from models import Student, Instructor, Course, Enrollment, engine

Session = sessionmaker(bind=engine)
session = Session()

def add_student():
    name = input("Enter student's name: ")
    email = input("Enter student's email: ")
    
    student = Student(name=name, email=email)
    try:
        session.add(student)
        session.commit()
        print(f"Student {name} added successfully!")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

def add_instructor():
    name = input("Enter instructor's name: ")
    department = input("Enter instructor's department: ")
    
    instructor = Instructor(name=name, department=department)
    session.add(instructor)
    session.commit()
    print(f"Instructor {name} added successfully!")

def add_course():
    title = input("Enter course title: ")
    description = input("Enter course description: ")
    instructor_id = input("Enter instructor ID for this course: ")

    course = Course(title=title, description=description, instructor_id=instructor_id)
    try:
        session.add(course)
        session.commit()
        print(f"Course {title} added successfully!")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

def enroll_student():
    student_id = int(input("Enter student ID: "))
    course_id = int(input("Enter course ID: "))
    
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    
    # Check if the student is already enrolled in the course
    existing_enrollment = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if existing_enrollment:
        print("Error: Student is already enrolled in this course.")
        return
    
    try:
        session.add(enrollment)
        session.commit()
        print("Student enrolled in course successfully!")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

def list_students():
    students = session.query(Student).all()
    if students:
        print("List of students:")
        for student in students:
            print(f"ID: {student.id}, Name: {student.name}, Email: {student.email}")
    else:
        print("No students found.")

def list_courses():
    courses = session.query(Course).all()
    if courses:
        print("List of courses:")
        for course in courses:
            instructor_name = course.instructor.name if course.instructor else "No Instructor"
            print(f"ID: {course.id}, Title: {course.title}, Instructor: {instructor_name}")
    else:
        print("No courses found.")

def list_instructors():
    instructors = session.query(Instructor).all()
    if instructors:
        print("List of instructors:")
        for instructor in instructors:
            print(f"ID: {instructor.id}, Name: {instructor.name}, Department: {instructor.department}")
    else:
        print("No instructors found.")

def list_student_courses():
    student_id = int(input("Enter student ID: "))
    
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Error: Student ID does not exist.")
        return
    
    enrollments = session.query(Enrollment).filter_by(student_id=student_id).all()
    if enrollments:
        print(f"Courses for student {student.name}:")
        for enrollment in enrollments:
            course = enrollment.course
            print(f"Course ID: {course.id}, Title: {course.title}, Instructor: {course.instructor.name}")
    else:
        print(f"Student {student.name} is not enrolled in any courses.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. Add a new student")
        print("2. Add a new instructor")
        print("3. Add a new course")
        print("4. Enroll a student in a course")
        print("5. See a list of all students")
        print("6. See a list of all courses")
        print("7. See a list of all instructors")
        print("8. See the list of courses a student is enrolled in")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            add_instructor()
        elif choice == '3':
            add_course()
        elif choice == '4':
            enroll_student()
        elif choice == '5':
            list_students()
        elif choice == '6':
            list_courses()
        elif choice == '7':
            list_instructors()
        elif choice == '8':
            list_student_courses()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
