from classes.person import Person
from classes.file_handler import FileHandler


class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    def __str__(self):
        return f"{self.name.upper()}\n---------------\nage: {self.age}\nid: {self.school_id}"

    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.role}, {self.school_id}, {self.password})"

    @classmethod
    def all_members(cls):
        students = []
        students_data = FileHandler.load_file("students")
        for member in students_data:
            new_student = cls(**member)
            students.append(new_student)
        return students


if __name__ == "__main__":
    students = Student.all_students()
    print(students)
