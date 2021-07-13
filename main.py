import os

for path in os.listdir():
    if path == "test2":
        os.chdir(path)
        for item in os.listdir():
            if item == "text.txt":
                os.remove(item)
