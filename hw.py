import os
import sys

path = os.getcwd()
create_folders = os.path.join(f"{path}/dir/dir1")
os.makedirs(create_folders)
path = create_folders
os.mkdir(os.path.join(f"{path}/dir2"))
os.makedirs(os.path.join(f"{path}/dir3/dir4"))
os.chdir("dir")
file = open("File.txt", "x")
file.close()
os.chdir("..")
path = os.getcwd()
print("CREATED!")

choice = input("delete(y/n): ")
if choice == "y":
    os.chdir("dir")
    os.remove("File.txt")
    os.chdir("dir1")
    os.rmdir("dir2")
    os.chdir("dir3")
    os.rmdir("dir4")
    os.chdir("..")
    os.rmdir("dir3")
    os.chdir("..")
    os.rmdir("dir1")
    os.chdir("..")
    os.rmdir("dir")
elif choice == "n":
    print("bye")
    sys.exit()
else:
    print("????")
    sys.exit()