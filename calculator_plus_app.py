import math

class Calculator:
    
    def square_root(self, x):
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()
    
num3 = 25
print(f"The square root of {num3} = {calculator.square_root(num3)}")

