import requests

py1 = "https://external-content.duckduckgo.com/iu/" \
      "?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.CLVLDcGHFGA2qCspd1SrrgHaD4%26pid%3DApi&f=1"
py2 = "https://external-content.duckduckgo.com/iu/" \
      "?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.xU6VOYH5N8vkJGTiTH8_mwHaEn%26pid%3DApi&f=1"
py3 = "https://external-content.duckduckgo.com/iu/" \
      "?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.tbKoKx5OHDJkn8Cja6gO9QHaEM%26pid%3DApi&f=1"
py4 = "https://external-content.duckduckgo.com/iu/" \
      "?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.cmyB7KgZrp-BJL-ycJBoyQHaEK%26pid%3DApi&f=1"
py5 = "https://external-content.duckduckgo.com/iu/" \
      "?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.3uGYsyH3X1tNF8gTmDgmmAHaFp%26pid%3DApi&f=1"

with open("py_img_1.png", "wb") as file:
    response = requests.get(py1)
    file.write(response.content)

with open("py_img_2.png", "wb") as file:
    response = requests.get(py2)
    file.write(response.content)

with open("py_img_3.png", "wb") as file:
    response = requests.get(py3)
    file.write(response.content)

with open("py_img_4.png", "wb") as file:
    response = requests.get(py4)
    file.write(response.content)

with open("py_img_5.png", "wb") as file:
    response = requests.get(py5)
    file.write(response.content)

print("Done!")