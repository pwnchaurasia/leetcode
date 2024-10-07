from lld.food_delivery.enums import OrderStatuses
from lld.food_delivery.menu import Menu
from lld.food_delivery.notification import Notification
from lld.food_delivery.notification_service import NotificationService


class Order:
    orders = []
    def __init__(self, user, restaurant, menu_items):
        self.user = user
        self.restaurant = restaurant
        self.menu_items = menu_items
        self.order_cost = None
        self.status = OrderStatuses.PENDING
        # self.menu_instance()
        self.total_cost()
        Order.orders.append(self)  # Keep track of all orders

    def order_details(self):
        return {
            'user': self.user,
            'restaurant': self.restaurant,
            'menu_items': self.menu_items,
            'status': self.status,
            'order_cost': self.order_cost,
        }

    def total_cost(self):
        total_cost = 0
        for item in self.menu_items:
            total_cost += item['item_name'].item_price * item['quantity']
        self.order_cost = total_cost

    def menu_instance(self):
        items = []
        for m_i in self.menu_items:
            [item for item in Menu.menus if item['item_name'] == m_i['item_name'] and item['restaurant'] == self.restaurant]


    def update_status(self, new_status):
        """
        Update the order status and send notifications.
        """
        self.status = new_status
        self.send_notifications()

    def send_notifications(self):
        """
        Send notifications to the user and restaurant about the order status change.
        """
        NotificationService.notify_user(self.user, f"Your order status has been updated to {self.status.value}.")
        NotificationService.notify_restaurant(self.restaurant.user,
                                              f"Order for {self.user.name} has been updated to {self.status.value}.")

    def assign_delivery_person(self, delivery_person):
        self.delivery_person = delivery_person
        self.status = OrderStatuses.OUT_FOR_DELIVERY
        NotificationService.notify_user(self.user, "Your order is out for delivery.")
        NotificationService.notify_delivery_person(delivery_person, f"New order {self} assigned to you.")



class OrderProperty:
    def __init__(self, delivery_address, driver, order):
        self.delivery_address = delivery_address
        self.driver = driver
        self.order = order