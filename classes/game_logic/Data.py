from Inc import Inc


class Data:
    _instance = None

    @staticmethod
    def get_instance():
        if Data._instance is None:
            Data()
        return Data._instance

    def __init__(self):
        if Data._instance is not None:
            raise Exception("You cannot create second singleton class")
        else:
            Data._instance = self

        self.lemonShop_inc = Inc("Lemon Shop", 5, 1, 1, 1,"")
        self.paper_inc = Inc("News Paper Shop", 10, 2, 2, 2, "")
        self.car_wash_inc = Inc("Car Wash", 15, 3, 3, 2, "")
        self.pizza_inc = Inc("Pizza", 20, 4, 4, 4, "")
        self.donut_inc = Inc("Donut Shop", 25, 5, 5, 5, "")
        self.sea_food_inc = Inc("Sea Food Rest", 30, 6, 6, 6, "")
        self.hokey_inc = Inc("Hokey Club", 35, 7, 7, 7, "")
        self.camera_inc = Inc("Cinema", 40, 8, 8, 8, "")
        self.white_house_inc = Inc("White House", 45, 9, 9, 9, "")
        self.oil_inc = Inc("Oil Company", 50, 10, 10, 10, "")
