class shop:
    def __init__(self):
        self.items={}
        
    def add(self,item_name,item_price):
        if item_name in self.items:
            self.items[item_name] +=item_price
        else:
            self.items[item_name] = item_price
            
    def rem(self,item_name):
        if item_name in self.items:
            del self.items[item_name]
            
    def total(self):
        total=sum(self.items.values())
        return total
    
    def show(self):
        print("\nShopping Cart:")
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")

cart=shop()
cart.add("1",10)
cart.add("2",20)
cart.add("3",15)

cart.show()

cart.rem("2")
print("\n After removing item 2:")
cart.show()

total=cart.total()
print(f"\nTOtal price: {total:.2f}")
        
