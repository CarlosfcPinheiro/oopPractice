# Creating classes
# Base class =================
class Product:
    def __init__(self, quantity:int, price:float) -> None:
        self.quantity = quantity
        self.price = price

# Derived/Child class ================
class Ball(Product):
    def __init__(self, quantity:int, price:float, color:str) -> None:
        # To give the access to change the parent __init__ method
        super().__init__(quantity, price)
        self.color = color

class Scratcher(Product):
    pass

class Portion(Product):
    pass