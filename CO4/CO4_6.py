class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)


class Sem1(Student):
    def __init__(self, name, age, mark):
        super().__init__(name, age)
        self.mark = mark

    def display(self):
        super().display()
        print("Mark:", self.mark)


class Result(Sem1):
    def __init__(self, name, age, mark, grade):
        super().__init__(name, age, mark)
        self.grade = grade

    def display(self):
        super().display()
        print("Grade:", self.grade)


s = Result("John", 20, 85, "A")
s.display()

