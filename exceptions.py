"""_summary_
    """
try:
    file = open("basics.py")
    numbers = (1, 2)
    numbers[0] = 4
    print(numbers[3])
except (IndexError, TypeError) as ex:
    print("Index not found")
    print(ex)
    print(type(ex))
except TypeError:
    print("Index not found")
else:
    print("Index found")
finally:
    print("closing file")
    file.close()

# ya no es necesario finally block, siempre que la clase implemente los metodos de __enter__ y __exit__
try:
    with open("basics.py") as file:
        pass
    numbers = (1, 2)
    numbers[0] = 4
    print(numbers[3])
except (IndexError, TypeError) as ex:
    print("Index not found")
    print(ex)
    print(type(ex))
except TypeError:
    print("Index not found")
else:
    print("Index found")


def calculate_xfactor(age) -> int:
    """_summary_

    Args:
        age (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        int: _description_
    """
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
