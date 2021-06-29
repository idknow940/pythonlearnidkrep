import random

string = "python"


class Main:
    def __init__(self, txt):
        self.str = txt
        self.dict = {}

        for i in self.str:
            self.dict[i] = i

        for i, j in self.dict.items():
            j = random.randint(0, 3)
            self.dict[i] = j
        print(self.dict)

    def rem_dup(self):
        res = {}
        for i, j in self.dict.items():
            if j not in res.values():
                res[i] = j
        self.dict = res
        print(res)

    def print_only_3_highest(self):
        lst = []
        for i in self.dict.values():
            lst.append(i)
        lst.sort()
        print(lst[-3:])


obj = Main(string)

print(obj.rem_dup())
print(obj.print_only_3_highest())
