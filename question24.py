def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Check if dividing by zero
        if num2 == 0:
            return "Error: Division by zero!"
        result = num1 / num2
    else:
        return "Error: Invalid operator!"
    
    return result

def main():
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")
        
        result = calculator(num1, num2, operator)
        print(f"{num1} {operator} {num2} = {result}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
