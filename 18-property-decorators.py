
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute with convention
    
    # Getter using @property
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter using @price.setter
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price can't be negative. Not updating.")
        else:
            print("Setting price...")
            self._price = value

    # Deleter using @price.deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# 🔍 Let's test it out
p = Product(100)
print(p.price)       # Getting price...
p.price = 150        # Setting price...
print(p.price)       # Getting price...
p.price = -20        # Error handled
del p.price          # Deleting price...
# print(p.price)     # Would throw AttributeError (uncomment to test)
