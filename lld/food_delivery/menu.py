
class Menu:
    menus = []
    def __init__(self, item_name, item_price, restaurant):
        self.item_name = item_name
        self.item_price = item_price
        self.restaurant = restaurant

    @classmethod
    def add(cls, menu):
        """
            Add a menu item from a specific restaurant
        """
        cls.menus.append(menu)

    @classmethod
    def remove(cls, item_name, restaurant):
        """
            Remove a menu item from a specific restaurant
        """
        cls.menus = [item for item in Menu.menus if item['item_name'] != item_name and  item['restaurant'] != restaurant]

