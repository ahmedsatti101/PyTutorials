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
        
    # Allows us to display the name of our objects
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        
item1 = Item("Phone", 100, 2)
item2 = Item("Laptop", 1000, 5)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

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