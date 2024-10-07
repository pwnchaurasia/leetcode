from lld.food_delivery.enums import OrderStatuses
from lld.food_delivery.notification_service import NotificationService
from lld.food_delivery.order import Order
from lld.food_delivery.payment_service import PaymentService


class OrderService:
    @staticmethod
    def create_order(user, restaurant, menu_items):
        charge_type = user.charge_type
        order = Order(user=user, restaurant=restaurant, menu_items=menu_items)
        order_cost = order.order_cost
        payment = PaymentService.payment(user, restaurant, charge_type, order_cost)
        if payment:
            order.update_status(OrderStatuses.CONFIRMED)
            print("Order confirmed")
            return order
        else:
            print("Payment failed try again!!!")
            return None

    @staticmethod
    def update_order_status(order, new_status):
        """
        Update the status of the given order and send notifications.
        """
        order.update_status(new_status)
        print(f"Order status updated to {new_status}.")

    @staticmethod
    def cancel_order(order):
        """
        Cancel the given order and notify the user and restaurant.
        """
        order.update_status(OrderStatuses.CANCELLED)
        NotificationService.notify_user(order.user, "Your order has been cancelled.")
        NotificationService.notify_restaurant(order.restaurant.user, "An order has been cancelled.")
        print("Order has been cancelled.")

    @staticmethod
    def get_order_details(order):
        return order.order_details()


