# 1

# import json
# import yaml
#
# choice = input("yaml or json?: ")
# if choice == "json":
#     with open("hw.json", "r") as jj:
#         data_json = json.load(jj)
#
#     with open("hw.txt", "w") as jt:
#         json.dump(data_json, jt, indent=4)
#
#     with open("main.yaml", "w") as jy:
#         yaml.dump(data_json, jy)
# elif choice == "yaml":
#     with open("main.yaml", "r") as yy:
#         data_yaml = yaml.load(yy)
#
#     with open("hw.json", "w") as yj:
#         json.dump(data_yaml, yj, indent=4)
#
#     with open("hw.txt", "w") as yt:
#         yaml.dump(data_yaml, yt, indent=4)
# else:
#     print(":/")

# 2

# import requests
#
# with open("hw.txt", "r") as file:
#     txt = file.read()
#
#
# class Methods:
#     def __init__(self, text):
#         self.links = text.split("\n")
#
#     def download_links(self):
#         for i in self.links:
#             response = requests.get(i)
#             num = 0
#             with open(f"img{num}.png", "wb") as F:
#                 F.write(response.content)
#             num += 1
#
#     def download_links_jpeg(self):
#         num = 0
#         for i in self.links:
#             if "jpg" in i or "JPG" in i:
#                 response = requests.get(i)
#                 with open(f"img{num}.jpg", "wb") as f:
#                     f.write(response.content)
#                 num += 1
#
#     def download_links_png(self):
#         num = 0
#         for i in self.links:
#             if "png" in i or "PNG" in i:
#                 response = requests.get(i)
#                 with open(f"img{num}.png", "wb") as f:
#                     f.write(response.content)
#                 num += 1
#
#
# py_imgs = Methods(txt)
#
# py_imgs.download_links_jpeg()
# py_imgs.download_links_png()
