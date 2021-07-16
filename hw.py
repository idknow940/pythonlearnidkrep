import os
import sys
import json

line = 0

output = ""
final_price = 0
final_quantity = 0
products = []
while True:
    data = input("name, price, quantity: ").split()
    dict_product = dict(
        name=data[0],
        price=data[1],
        quantity=data[2]
    )
    final_price += int(data[1])
    final_quantity += int(data[2])
    dict_end = dict(
        final_price=final_price,
        final_quantity=final_quantity
    )
    line += 1
    output += f"{line}: {dict_product}\n"
    end = input("leave the loop(y/n): ")
    products.append(dict_product)
    if end == "y":
        products.append(dict_end)
        break
    elif end == "n":
        pass
    else:
        print("????")
        sys.exit()

with open("product.json", "w") as pj:
    json.dump(products, pj, indent=4)
    print("Added your product to the .json file!")
