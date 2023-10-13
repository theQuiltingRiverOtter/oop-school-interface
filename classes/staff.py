from classes.person import Person
from classes.file_handler import FileHandler

# from person import Person
# from file_handler import FileHandler


class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    def __str__(self):
        return f"Staff: {self.name}, Age: {self.age}, Role: {self.role}, ID: {self.employee_id}"

    def __repr__(self):
        return f"Staff({self.name}, {self.age}, {self.role}, {self.employee_id}, {self.password})"

    @classmethod
    def all_staff(cls):
        all_staff = []
        staff = FileHandler.load_file("staff")
        for member in staff:
            new_staff = cls(**member)
            all_staff.append(new_staff)
        return all_staff


if __name__ == "__main__":
    # staff = Staff.all_staff()
    staff_data = {
        "name": "culpepper",
        "age": "25",
        "role": "Principal",
        "employee_id": "86545",
        "password": "xx",
    }

    staff1 = Staff(**staff_data)
    print(staff1.role)
