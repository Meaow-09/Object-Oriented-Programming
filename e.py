def divide(x, y):
    print("Dividing")
    return x / y


def calculate(a, b):
    print("Calculating")
    try:
        result = divide(a, b)
        print("Result:", result)
    except ZeroDivisionError:
        print("You can't divide a number by zero!")
    except TypeError:
        print("You should divide a number by a number!")
    except Exception as e:
        print("Error occured:", e)
    finally:
        print("Closing")


if __name__ == "__main__":
    calculate(10, 2)
    calculate(10, 'a')
