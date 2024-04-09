class Sandwich:
    def __init__(self) -> None:
        self._bread = None
        self._meat = None
        self._cheese = None
        self._vegies = []
        self._sauces = []
    
    def __str__(self) -> str:
        ingredients = f"Bread : {self._bread} meat: {self._meat}"
        if self._cheese:
            ingredients += f" Cheese: {self._cheese}"
        ingredients += " Vegies : " + ", ".join(self._vegies)
        ingredients += " sauces : " + ", ".join(self._sauces)
        return ingredients

class SandwichBuilder:
    def __init__(self) -> None:
        self.sandwich = Sandwich()
    
    def add_bread(self):
        pass

    def add_meat(self):
        pass

    def add_cheese(self):
        pass

    def add_vegies(self):
        pass

    def add_sauces(self):
        pass

    
    def get_sandwich(self):
        return self.sandwich

class ClubSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "White Bread"

    def add_meat(self):
        self.sandwich._meat = "Chicken"
    
    def add_cheese(self):
        self.sandwich._cheese = "Cheddar"
    
    def add_vegies(self):
        self.sandwich._vegies.append("Tomato")
        self.sandwich._vegies.append("Lettuce")
    
    def add_sauces(self):
        self.sandwich._sauces.append("mayo")
        self.sandwich._sauces.append("mustard")



class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich._bread = "Whole Whead Bread"

    def add_meat(self):
        self.sandwich._meat = "Tofu"
    
    # def add_cheese(self):
    #     self.sandwich._cheese = "Cheddar"
    
    def add_vegies(self):
        self.sandwich._vegies.append("Spinanch")
        self.sandwich._vegies.append("Bell Pepper")
    
    def add_sauces(self):
        self.sandwich._sauces.append("Hummus")
        self.sandwich._sauces.append("Tahini")


class Waiter:
    def __init__(self) -> None:
        self.sandwich_builder = None

    def get_builder(self, builder):
        self.sandwich_builder = builder
    
    def create_sandwich(self):
        self.sandwich_builder.add_bread()
        self.sandwich_builder.add_meat()
        self.sandwich_builder.add_cheese()
        self.sandwich_builder.add_vegies()
        self.sandwich_builder.add_sauces()
    
    def serve_sandwich(self):
        return self.sandwich_builder.get_sandwich()
    



waiter = Waiter()
waiter.get_builder(ClubSandwichBuilder())

waiter.create_sandwich()
print("======= CLUB SANDWICH=======")
Sandwich1 = waiter.serve_sandwich()
print(Sandwich1)

waiter.get_builder(VeggieSandwichBuilder())

waiter.create_sandwich()
print("======= Vegies SANDWICH=======")
Sandwich2 = waiter.serve_sandwich()

print(Sandwich2)