import sys

text = input("enter a problem (separate with spaces): ")

list_text = text.split()

num1 = list_text[0]
num2 = list_text[2]

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
else:
    sys.exit()

operator = list_text[1]

res = 0

if operator == "*":
    res = num1 * num2
elif operator == "/":
    res = num1 / num2
elif operator == "+":
    res = num1 + num2
elif operator == "-":
    res = num1 - num2

print(res)
