import os
import sys
import json

# Variables
final_price = 0
final_quantity = 0
products = []

dct = {}

# Main Loop
while True:
    # Input
    data = input("name, price, quantity(separate with ', '): ").split(",")

    # Main Info
    dict_product = dict(
        name=data[0],
        price=data[1],
        quantity=data[2]
    )

    # Final Variables
    final_price += float(data[1])
    final_quantity += float(data[2])

    # Final Dict
    dict_end = dict(
        final_price=final_price,
        final_quantity=final_quantity
    )

    products.append(dict_product)

    # Leave Logic

    # Input
    end = input("leave the loop(y/n): ")

    # Statements
    if end == "y":
        products.append(dict_end)
        dct["items"] = products
        break
    elif end == "n":
        pass
    else:
        print("????")
        sys.exit()

# Dumping Products List In product.json
with open("hw.json", "w") as pj:
    json.dump(dct, pj, indent=4)
    print("Written your product to the .json file!")

with open("hw.json", "r") as pj:
    print(f"The dictionary you wrote: {json.load(pj)}")
