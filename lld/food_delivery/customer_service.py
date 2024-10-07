from lld.food_delivery.menu import Menu
from lld.food_delivery.restaurant_service import RestaurantService
from lld.food_delivery.resturants import Restaurant


class CustomerService:

    @staticmethod
    def find_restaurants(restaurant_name=None, restaurant_address=None):
        return RestaurantService.find_restaurants(restaurant_name, restaurant_address)

    @staticmethod
    def find_menu(restaurant):
        return RestaurantService.find_menu(restaurant)

    @staticmethod
    def order_cart(restaurant_id, item_name):
        pass

