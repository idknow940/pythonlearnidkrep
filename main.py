class Human(object):
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def present(self):
        return f"Loading . . .\n{self.name}, {self.surname}, {self.age}"


human = Human("John", "Dohn", 258)


class Student(Human):
    def __init__(self, name: str, surname: str, age: int, uni: str) -> None:
        print("Student")
        # super(Student, self).__init__(name, surname, age)
        super().__init__(name, surname, age)
        # Human.__init__(self, name, surname, age)
        self.uni = uni

    def present(self):
        return "lol"


class Employee(Human):
    def __init__(self, name: str, surname: str, age: int, work: str) -> None:
        print("Employee")
        # super(Student, self).__init__(name, surname, age)
        super().__init__(name, surname, age, work)
        # Human.__init__(self, name, surname, age)
        self.work = work


class EconomyStudent(Student):
    def __init__(self, name: str, surname: str, age: int, uni: str) -> None:
        super().__init__(name, surname, age, uni)


class Mixed(Employee, Student):
    def __init__(self, name: str, surname: str, age: int, work: str, uni: str) -> None:
        # Employee.__init__(self, name, surname, age, work)
        # Student.__init__(self, name, surname, age, uni)
        super().__init__(name, surname, age, uni)
        self.all_list = [self.name, self.surname, str(self.age), self.work, self.uni]

    def present(self):
        a = ""
        for i in self.all_list:
            a += i
            if i != "IDIOT UNI":
                a += ", "
        return a


mix_guy = Mixed("JOE", "WHITE", 256, "IDIOT.CORP", "IDIOT UNI")
print(mix_guy.present())
