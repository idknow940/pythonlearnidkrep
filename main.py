# class Resume:
#     def __init__(self, name, surname, birthday, serial_number, password):
#         self.name = name
#         self.surname = surname
#         self.birthday = birthday
#         self._serial_number = serial_number
#         self.__password = password
#
#     @property
#     def age(self) -> int:
#         return 2021 - self.birthday
#
#     @property
#     def serial_number(self) -> str:
#         return f"XXXX XXXX XXXX {self._serial_number[-4:]}"
#
#     @property
#     def password(self) -> str:
#         a = "*"
#         for i in range(len(self.__password)):
#             a += "*"
#         return a
#
#
# someone = Resume("Alek", "Aleksanyan", 2008, "1111555566668456", "LOLHAMONASdnAKNKDSNKWA")
# print("{}".format(someone.serial_number))
# print("{}".format(someone.password))

tuple_ = (
    1, 2, 3, 5, 8
)

list_ = [i for i in tuple_ if i % 2 == 0]
dict_ = {key: key**key for key in tuple_}
print(list_, dict_)
