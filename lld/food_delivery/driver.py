# --- Driver Code ---
from lld.food_delivery.customer_service import CustomerService
from lld.food_delivery.enums import ChargeTypes, OrderStatuses
from lld.food_delivery.menu import Menu
from lld.food_delivery.order import Order
from lld.food_delivery.order_service import OrderService
from lld.food_delivery.payment_service import PaymentService
from lld.food_delivery.restaurant_service import RestaurantService
from lld.food_delivery.users import Customer, RestaurantOwner, DeliveryPerson


def main():
    # Create Users
    print("\n--- Creating Users ---")
    customer = Customer(name="Alice", email="alice@example.com", password="password123")
    owner = RestaurantOwner(name="Bob", email="bob@restaurant.com", password="password456")
    delivery_person = DeliveryPerson(name="Charlie", email="charlie@delivery.com", password="password789")

    # Assign payment details to customer
    customer.card_number = "1234567812345678"
    customer.charge_type = ChargeTypes.CARD.value

    # Assign payment details to owner if needed (not used in this example)
    # Assign payment details to delivery person if needed (not used in this example)

    # Owner adds a restaurant
    print("\n--- Owner Adding Restaurants ---")
    restaurant1 = owner.add_restaurant(restaurant_name="Pizza Palace", address="456 Elm St")
    restaurant2 = owner.add_restaurant(restaurant_name="Burger Shack", address="789 Oak St")

    # Owner adds menu items to restaurants
    print("\n--- Adding Menu Items ---")
    menu1 = Menu(item_name="Pepperoni Pizza", item_price=12.99, restaurant=restaurant1)
    Menu.add(menu1)
    menu2 = Menu(item_name="Margherita Pizza", item_price=10.99, restaurant=restaurant1)
    Menu.add(menu2)
    menu3 = Menu(item_name="Cheeseburger", item_price=8.99, restaurant=restaurant2)
    Menu.add(menu3)
    menu4 = Menu(item_name="Veggie Burger", item_price=7.99, restaurant=restaurant2)
    Menu.add(menu4)

    # Customer searches for restaurants
    print("\n--- Customer Searching for Restaurants ---")
    search_results = CustomerService.find_restaurants(restaurant_name="Pizza Palace")
    print(f"Search Results: {[rest.restaurant_name for rest in search_results]}")

    # Customer searches for menu items in a restaurant
    print("\n--- Customer Viewing Menu ---")
    menu_items = CustomerService.find_menu(restaurant1)
    print(f"Menu for {restaurant1.restaurant_name}: {[item.item_name for item in menu_items]}")

    # Customer places an order
    print("\n--- Customer Placing Order ---")
    order_details = [
        {'item_name': menu1, 'quantity': 2},
        {'item_name': menu2, 'quantity': 1}
    ]
    order = customer.place_order(restaurant=restaurant1, menu_items=order_details)
    if order:
        print(f"Order Placed: {order}")
    else:
        print("Order placement failed.")

    # Delivery person accepts the order
    print("\n--- Delivery Person Accepting Order ---")
    if delivery_person.accept_order(order):
        print(f"{delivery_person.name} accepted the order.")
    else:
        print(f"{delivery_person.name} could not accept the order.")

    # Delivery person updates order status to IN_PROGRESS
    print("\n--- Delivery Person Updating Order Status to IN_PROGRESS ---")
    delivery_person.update_delivery_status(OrderStatuses.OUT_FOR_DELIVERY)

    # Delivery person updates order status to DELIVERED
    print("\n--- Delivery Person Updating Order Status to DELIVERED ---")
    delivery_person.update_delivery_status(OrderStatuses.DELIVERED)

    # View Order Details
    print("\n--- Viewing Order Details ---")
    order_info = OrderService.get_order_details(order)
    print(order_info)

    # List All Orders
    print("\n--- Listing All Orders ---")
    print(Order.orders)

    # List All Payments
    print("\n--- Listing All Payments ---")
    print(PaymentService.list_all_payments())

    # List All Restaurants
    print("\n--- Listing All Restaurants ---")
    print(RestaurantService.list_restaurants())

    # List All Menu Items
    print("\n--- Listing All Menu Items ---")
    print(Menu.menus)


if __name__ == "__main__":
    main()