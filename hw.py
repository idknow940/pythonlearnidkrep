class Country:
    def __init__(self, country_name, continent):
        self.country_name = country_name
        self.continent = continent

    def present_country(self):
        return f"country_name: {self.country_name}, continent: {self.continent}"


class Brand:
    def __init__(self, brand_name, start_date):
        self.brand_name = brand_name
        self.start_date = start_date

    def present_brand(self):
        return f"brand_name: {self.brand_name}, start_date: {self.start_date}"


class Season:
    def __init__(self, season_name, temp):
        self.season_name = season_name
        self.temp = temp

    def present_season(self):
        return f"season_name: {self.season_name}, temperature: {self.temp}"


class Product(Season, Brand, Country):
    def __init__(self, country_name, continent, brand_name, start_date, season_name, temp, product_name,
                 product_type, product_quantity, product_price, discount):
        Season.__init__(self, season_name, temp)
        Brand.__init__(self, brand_name, start_date)
        Country.__init__(self, country_name, continent)
        self.product_name = product_name
        self.product_type = product_type
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_discount = discount

    def present_product(self):
        a = ""
        items = {"product_name": self.product_name, "product_type": self.product_type,
                 "product_quantity": str(self.product_quantity), "product_price": str(self.product_price),
                 "season_name": self.season_name, "temperature": self.temp, "brand_name": self.brand_name,
                 "start_date": self.start_date, "country_name": self.country_name, "continent_name": self.continent}
        for key, value in items.items():
            key += ": " + value + "; "
            a += key
        return a

    def add_quantity(self):
        self.product_quantity += 1

    def rem_quantity(self):
        self.product_quantity -= 1

    def calc_discount(self):
        return round(self.product_price - (self.product_price * self.product_discount / 100))


product = Product("Armenia", "Asia/Europe", "Unhelpfulo", "1865", "Moon", "-137 - -100",
                  "MoonWalker", "Shoes", 0, 50000000, 50)

print(product.present_product())

for i in range(0, 50):
    product.add_quantity()

for i in range(0, 20):
    product.rem_quantity()

print(product.product_quantity)
print(product.calc_discount())
