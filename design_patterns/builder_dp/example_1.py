class House:
    def __init__(self) -> None:
        self.floor = None
        self.wall = None
        self.roof = None
        self.furniture = {}
    
    def __str__(self) -> str:
        return f" Floor {self.floor} Wall: {self.wall} roof : {self.roof} furniture : {self.furniture}"


class HouseBuilder:
    def __init__(self) -> None:
        self.house = House()
    
    def set_floor(self, count):
        self.house.floor = count
        return self
    
    def set_wall(self, count):
        self.house.wall = count
        return self
    
    def set_roof(self, count):
        self.house.roof = count
        return self

    def get_house(self):
        return self.house

    def set_furniture(self, name, amount):
        if not self.house.furniture.get(name):
            self.house.furniture[name] = 0
        self.house.furniture[name] += amount
        return self


print("==========SMALL HOUSE ===============")

small_house_builder = HouseBuilder()
small_house_builder.set_floor(5).set_wall(10).set_roof(25).set_furniture("chair", 5).set_furniture("chair", 15)
small_house = small_house_builder.get_house()
print(small_house)


print("==========BIG HOUSE ===============")

big_house_builder = HouseBuilder()
big_house_builder.set_floor(15).set_wall(50).set_roof(50).set_furniture("table", 5).set_furniture("chair", 5)
big_house = big_house_builder.get_house()
print(big_house)