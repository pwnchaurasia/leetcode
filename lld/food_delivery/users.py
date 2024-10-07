from lld.food_delivery.enums import UserTypes, OrderStatuses
from lld.food_delivery.order_service import OrderService
from lld.food_delivery.restaurant_service import RestaurantService
from lld.food_delivery.resturants import Restaurant


class User:
    users = []
    def __init__(self, name, email, password, user_type):
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type

    def add_user(self):
        data = {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
        User.users.append(data)

    def __repr__(self):
        return f"{self.user_type.value}({self.name}, {self.email})"


class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, UserTypes.CUSTOMER)
        self.order_history = []

    def place_order(self, restaurant, menu_items):
        order = OrderService.create_order(user=self, restaurant=restaurant, menu_items=menu_items)
        if order:
            self.order_history.append(order)
        return order

    def view_order_history(self):
        return self.order_history



class RestaurantOwner(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, UserTypes.OWNER)
        self.restaurants = []

    def add_restaurant(self, restaurant_name, address):
        restaurant = Restaurant(user=self, restaurant_name=restaurant_name, address=address)
        self.restaurants.append(restaurant)
        RestaurantService.add_restaurant(user=self, restaurant_name=restaurant_name, address=address)
        return restaurant

    def remove_restaurant(self, restaurant_name):
        self.restaurants = [rest for rest in self.restaurants if rest.restaurant_name != restaurant_name]
        RestaurantService.remove_restaurant(restaurant_name)



class DeliveryPerson(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password, UserTypes.DELIVERY_PERSON)
        self.current_order = None

    def accept_order(self, order):
        if self.current_order is None and order.status == OrderStatuses.CONFIRMED:
            self.current_order = order
            order.assign_delivery_person(self)
            order.update_status(new_status=OrderStatuses.OUT_FOR_DELIVERY)
            return True
        return False

    def update_delivery_status(self, new_status):
        if self.current_order:
            self.current_order.update_status(new_status)
            if new_status == OrderStatuses.DELIVERED:
                self.current_order = None


class UserFactory:
    @staticmethod
    def create_user(name, email, password, user_type: UserTypes):
        if user_type == UserTypes.CUSTOMER:
            return Customer(name, email, password)
        elif user_type == UserTypes.OWNER:
            return RestaurantOwner(name, email, password)
        elif user_type == UserTypes.DELIVERY_PERSON:
            return DeliveryPerson(name, email, password)
        else:
            raise ValueError("Invalid user type")