
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y

def run_calculator():
    calc = Calculator()
    
    print("This is the beginning of calculation made easy #Python Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            print(f"Result: {calc.add(num1, num2)}")
        elif operation == '-':
            print(f"Result: {calc.subtract(num1, num2)}")
        elif operation == '*':
            print(f"Result: {calc.multiply(num1, num2)}")
        elif operation == '/':
            print(f"Result: {calc.divide(num1, num2)}")
        else:
            print("Invalid operation selected.")

    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    
    finally:
        choice = input("\nDo you want to make another calculation? (yes/no): ").lower()
        if choice== 'no':
            print("See you next time!! Don't forget to smile")
        
if __name__ == "__main__":
    run_calculator()
    
