class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

# Create a Calculator object with two numbers
calc = Calculator(5, 10)

# Call the add method on the Calculator object to get the sum of the two numbers
sum = calc.add()

print("The sum is:", sum)
