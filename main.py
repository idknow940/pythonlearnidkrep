class Class(object):
    def __init__(self, name, sur_name):
        self.name = name
        self.surname = sur_name

    def present(self):
        print(f"hello im {self.name} {self.surname}")


obj_1 = Class("Alek", "Aleksanyan")

obj_1.present()