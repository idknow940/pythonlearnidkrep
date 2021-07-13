class Hotel:
    def __init__(self, hotel_name: str, place: str, mid_price: float, lux_price: float, mid1: str, mid2: str, mid3: str,
                 lux1: str, lux2: str, lux3: str, discount_hotel: int) -> None:
        try:
            self.hotel_name = str(hotel_name)
            self.place = str(place)
            self.mid1 = str(mid1)
            self.mid2 = str(mid2)
            self.mid3 = str(mid3)
            self.lux1 = str(lux1)
            self.lux2 = str(lux2)
            self.lux3 = str(lux3)
            self.mid_price = float(mid_price)
            self.lux_price = float(lux_price)
            self.discount = int(discount_hotel)
            self.room_mid = {"mid1": self.mid1, "mid2": self.mid2, "mid3": self.mid3}
            self.room_lux = {"lux1": self.lux1, "lux2": self.lux2, "lux3": self.lux3}
        except ValueError:
            raise ValueError("wrong value types for hotel.")

    def hotel_present(self):
        return "{} {} {} {} {} {}".format(self.name, self.place, self.mid_price, self.lux_price, self.room_mid,
                                          self.room_lux)

    def booking(self, type):
        if type == "mid":
            for mid, c in self.room_mid.items():
                if c == "free":
                    c = "busy"
                    return mid, c
        if type == "lux":
            for lux, c in self.room_lux.items():
                if c == "free":
                    c = "busy"
                    return lux, c

    def check_room(self):
        for i, v in self.room_mid.items():
            return f"{i}: {v}"
        for i, v in self.room_lux.items():
            return f"{i}: {v}"

    def hotel_discount(self):
        dis_mid = round(self.mid_price - (self.mid_price * self.discount / 100))
        dis_lux = round(self.lux_price - (self.lux_price * self.discount / 100))

        return f"mid: {dis_mid}, lux: {dis_lux}"


class Taxi:
    def __init__(self, taxi_name: str, car_types: str, price_for_tour: float, discount_taxi: int) -> None:
        try:
            self.taxi_name = str(taxi_name)
            self.types = str(car_types)
            self.price_for_tour = float(price_for_tour)
            self.discount = int(discount_taxi)
        except ValueError:
            raise ValueError("Wrong value types for taxi.")

    def taxi_present(self):
        return f"name: {self.name} types: {self.types} price for tour: {self.price_for_tour}"

    def taxi_discount(self):
        return round(self.price_for_tour - (self.price_for_tour * self.discount / 100))


class TourService(Hotel, Taxi):
    def __init__(self, name: str, hotel_name: str, hotel_place: str, mid_price: float, lux_price: float, price_for_tour,
                 mid1: str, mid2: str, mid3: str, lux1: str, lux2: str, lux3: str, discount_hotel: int,
                 taxi_name: str, car_types: str, discount_taxi: int) -> None:
        Hotel.__init__(self, hotel_name, hotel_place, mid_price, lux_price, mid1, mid2, mid3, lux1, lux2, lux3,
                       discount_hotel)
        Taxi.__init__(self, taxi_name, car_types, price_for_tour, discount_taxi)
        try:
            self.tour_name = str(name)
            self.price = float(self.price_for_tour)
            self.price_for_mid = round(self.price + self.mid_price)
            self.price_for_lux = round(self.price + self.lux_price)
        except ValueError:
            raise ValueError("Wrong value types for TourService.")

    def tourservice_present(self):
        return f"Hello, we are {self.tour_name} tour service,\nwe will provide you a tour to {self.place}" \
               f"where we will stay in {self.hotel_name},\nwe will go there with {self.taxi_name}" \
               f"taxi service, they will provide {self.types} types of taxis,\n" \
               f"lux price will be {self.price_for_lux},\n" \
               f"mid price will be {self.price_for_mid}, have a nice tour!"


print(TourService.__mro__)

tour = TourService("PyTour", "PyHotel", "Gyumri", 10000, 50000, 5000,
                   "free", "busy", "busy", "busy", "free", "free", 10,
                   "PyGo", "PyFlash", 10)

print(tour.tourservice_present())
