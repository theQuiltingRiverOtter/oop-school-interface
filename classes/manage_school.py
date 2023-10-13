from classes.school import School


class ManageSchool:
    def __init__(self, schoolName: str):
        self.school = School(schoolName)

    def main_menu(self):
        print("What would you like to do?")
        print("  Options")
        print("   1. List All Students")
        print("   2. View Individual Student <student_id>")
        print("   3. Add a student")
        print("   4. Remove a Student <student_id>")
        print("   5. Print Menu")
        print("   6. Quit")

    def get_student_data(self):
        student_data = {"role": "Student", "school_id": self.school.random_school_id()}
        student_data["name"] = input("Name: ")
        student_data["age"] = input("Age: ")
        student_data["password"] = input("Password: ")
        return student_data

    def execute(self):
        self.main_menu()
        while True:
            choice = input("Choice: ")
            if choice == "6":
                break
            if choice == "1":
                self.school.list_students()
            if choice == "2":
                school_id = input("Enter student_id: ")
                self.school.find_student_by_id(school_id)
            if choice == "3":
                student_data = self.get_student_data()
                self.school.add_student(student_data)
            if choice == "4":
                school_id = input("Enter student_id: ")
                self.school.remove_student(school_id)
            if choice == "5":
                self.main_menu()
