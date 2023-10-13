import csv


class FileHandler:
    def __init__(self):
        self.data = None

    @classmethod
    def load_file(self, filename):
        with open(f"data/{filename}.csv") as file:
            data = list(csv.DictReader(file, delimiter=","))
        self.data = data
        return self.data


if __name__ == "__main__":
    file_staff = FileHandler("staff")
    file_staff.load_file()
