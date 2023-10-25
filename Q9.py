class Calculator:
    def add(self, x, y):
        result=x+y
        print("Add =",result)

    def subtract(self, x, y):
        result=x-y
        print("Subtract =",result)

    def multiply(self, x, y):
        result=x*y
        print("Multiply =", result)

    def divide(self, x, y):
        result=x/y
        print("Divided =", result)
        

calculator = Calculator()
calculator.add(7, 5)
calculator.subtract(34, 21)
calculator.multiply(54, 2)
calculator.divide(144, 2)



