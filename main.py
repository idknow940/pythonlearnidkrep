class Class(object):
    def __init__(self, name, sur_name):
        self.name = name
        self.surname = sur_name


obj_1 = Class("Alek", "Aleksanyan")

print(f"{obj_1.name} {obj_1.surname}")