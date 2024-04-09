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



class SmallHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.set_floor("Small floor")

    def build_wall(self):
        self.set_floor("Small floor")

    def build_roof(self):
        self.set_floor("Small floor")
    
    def build_furniture(self):
        self.set_furniture("chair", 2)
        self.set_furniture("table", 10)
        self.set_furniture("lamp", 15)


class BigHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.set_floor("Big floor")

    def build_wall(self):
        self.set_floor("Big floor")

    def build_roof(self):
        self.set_floor("Big floor")
    
    def build_furniture(self):
        self.set_furniture("chair", 5)
        self.set_furniture("table", 15)
        self.set_furniture("lamp", 35)




class Contractor: # director
    def __init__(self, builder) -> None:
        self.builder = builder

    def construct_house(self):
        self.builder.build_floor()
        self.builder.build_wall()
        self.builder.build_floor()
        self.builder.build_furniture()






small_builder = SmallHouseBuilder()
big_builder = BigHouseBuilder()


small_contractor = Contractor(small_builder)
small_contractor.construct_house()


big_contractor = Contractor(big_builder)
big_contractor.construct_house()


print(small_builder.get_house())
print("==========")
print(big_builder.get_house())

