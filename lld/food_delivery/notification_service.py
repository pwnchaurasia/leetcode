from lld.food_delivery.notification import Notification


class NotificationService:
    @staticmethod
    def notify_user(user, message):
        Notification(user, message).send()

    @staticmethod
    def notify_restaurant(restaurant_user, message):
        Notification(restaurant_user, message).send()

    @staticmethod
    def notify_delivery_person(delivery_person, message):
        Notification(delivery_person, message).send()