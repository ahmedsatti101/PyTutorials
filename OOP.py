import csv
from unicodedata import name

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the recevied arguments
        assert price >= 0, f"Price {price} should be more than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} should be more than or equal to zero!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Assign to self object
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        # for item in items:
            # Item(
                # name=item.get('name'),
                # price=float(item.get('price')),
                # quantity=int(item.get('quantity')),
            #)
            
    def is_integer(num):
        #It will count out the floats that are point zero
        # i.e.: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    # Allows us to display the name of our objects
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        
print(Item.is_integer(7))

# Item.instantiate_from_csv()
# print(Item.all)
        

#for instance in Item.all: Print item name
    #print(instance.name)

#item1.apply_discount()
#print(item1.price)

#item2 = Item("Laptop", 1000, 5)
#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)

#print(Item.__dict__)  Prints all attributes at class level
#print(item1.__dict__) Prints all attributes at instance level