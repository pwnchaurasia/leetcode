from lld.food_delivery.menu import Menu
from lld.food_delivery.resturants import Restaurant


class RestaurantService:

    @staticmethod
    def find_restaurants(restaurant_name=None, restaurant_address=None):
        all_restaurants = Restaurant.restaurants
        if restaurant_name:
            all_restaurants = [rest for rest in all_restaurants if rest.restaurant_name == restaurant_name]
        if restaurant_address:
            # some proper logic to find the restaurants in a proper range say 5km range of user location
            all_restaurants = [rest for rest in all_restaurants if rest.restaurant_address <= restaurant_address]
        return all_restaurants

    @staticmethod
    def find_menu(restaurant):
        all_menus = Menu.menus
        all_menus = [menu for menu in all_menus if menu.restaurant == restaurant]
        if not all_menus:
            print("No menu available for restaurant_id {}".format(restaurant))
        return all_menus

    @staticmethod
    def add_restaurant(user, restaurant_name, address):
        restaurant = Restaurant(user=user, restaurant_name=restaurant_name, address=address)
        Restaurant.add_restaurant(restaurant)  # Now it's a class method
        print(f"Restaurant '{restaurant_name}' added successfully!")

    @staticmethod
    def remove_restaurant(restaurant_name):
        # Now the class method is called directly
        Restaurant.remove_restaurant(restaurant_name)
        print(f"Restaurant '{restaurant_name}' removed successfully!")

    @staticmethod
    def list_restaurants():
        return Restaurant.restaurants