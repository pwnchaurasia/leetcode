class Restaurant:
    restaurants = []
    def __init__(self, user, restaurant_name, address):
        self.user = user
        self.restaurant_name = restaurant_name
        self.address = address

    @classmethod
    def add_restaurant(cls, restaurant):
        # Add the current restaurant instance to the list of restaurants
        cls.restaurants.append(restaurant)

    @classmethod
    def remove_restaurant(cls, restaurant_name):
        Restaurant.restaurants = [rest for rest in Restaurant.get_restaurants() if rest.restaurant_name != restaurant_name]

    @classmethod
    def get_restaurants(cls):
        # Return the list of all restaurants
        return cls.restaurants