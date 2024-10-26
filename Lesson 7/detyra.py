def calculate(nr1, nr2, operator):
    if operator == '+':
        return nr1 + nr2
    elif operator == '-':
        return nr1 - nr2
    elif operator == '*':
        return nr1 * nr2
    elif operator == '/':
        if nr2 == 0:
            raise ZeroDivisionError("You can't divide by zero!")
        return nr1 / nr2
    else:
        raise ValueError("Invalid operator! Please use +, -, *, or /.")


def main():
    try:
        nr1 = float(input("Enter the first number: "))
        nr2 = float(input("Enter the second number: "))

        operator = input("Enter an operator (+, -, *, /): ")

        result = calculate(nr1, nr2, operator)

        print(f"The result is: {result}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("End of program.")

if __name__ == "__main__":
    main()
