# 1

# import requests
# import json
# import threading
#
#
# def download(name, line=0):
#     with open("hw.json", "r") as r:
#         txt = json.load(r)
#
#     with open(f"{name}.png", "wb") as f:
#         response = requests.get(txt[line])
#         f.write(response.content)
#
#
# threads = []
# for i in range(0, 10):
#     x = threading.Thread(target=download, args=(i, i))
#     x.start()
#     threads.append(x)
#
# [i.join() for i in threads]

# 2

# a = [
#     1, 2, 3, 4, 516, 1561, 156, 165, 81
# ]
#
# sum = 0
#
# for i in range(0, len(a), 1):
#     sum += a[i]
#
# print(sum)

# 3

# a = [1, 2, [3, 4]]
#
#
# def foo(list_):
#     sum = 0
#     for i in list_:
#         if isinstance(i, list):
#             sum += foo(i)
#         else:
#             sum += i
#     return sum
#
#
# print(foo(a))
