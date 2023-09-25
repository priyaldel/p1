class calculator:
    def add(self, x, y):
        return x+y
    def sub(self, x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        if y==0:
            return "div by 0: INVALID"
        return x/y
calculator = calculator()
x=int(input("Enter number1 :"))
y=int(input("Enter number2 :"))

print("Add", calculator.add(x,y))
print("Sub", calculator.sub(x,y))
print("Mul", calculator.mul(x,y))
print("Div", calculator.div(x,y))

    