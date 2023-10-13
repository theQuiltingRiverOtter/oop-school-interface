from classes.staff import Staff
from classes.student import Student
from random import randint


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_members()
        self.students = Student.all_members()

    def list_students(self):
        for idx, student in enumerate(self.students):
            print(f"{idx + 1}. {student.name} {student.school_id}")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                print(student)
                return student
        print("This ID doesn't match any students")
        return None

    def random_school_id(self):
        random_id = ""
        for i in range(6):
            random_id += str(randint(0, 9))

        return random_id

    def add_student(self, student_data):
        for key, val in student_data.items():
            if val == "":
                print(f"Need {key} value to add a student")
                return
        try:
            student = Student(**student_data)
            self.students.append(student)
            print(f"{student.name} was added")
        except:
            print(f"something went wrong")

    def remove_student(self, student_id):
        student = self.find_student_by_id(student_id)
        if student:
            self.students.remove(student)
            print(f"{student.name} successfully removed")
            return
