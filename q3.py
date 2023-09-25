class shop:
    def __init__(self):
        self.orig = {}
        self.x={}
        
    def add(self,name,price):
        self.orig[name]=price
        if name in self.x:
            self.x[name] +=price
        else:
            self.x[name] = price
            
    def rem(self,name):
        if name in self.x:
            del self.x[name]
            
    def total(self):
        total=sum(self.x.values())
        return total
    
    def show(self):
        print("\nShopping Cart:")
        for y, price in self.x.y():
            print(f"{x}: ${price:.2f}")

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
        