""" anotaciones """


x, y = 1, 2
print(x, y, type(x))

# type annotation, ayuda a definir el tipo de una variable
# pero igualmente puede cambiar su tipo reasignando su valor
z: float = 5.1
print(z, type(z))

# inmutable, los numeros y cadenas son inmutables
H = 1234
print(H, id(H))  # 1234 2853530676272
H += 1
print(H, id(H))  # 1235 2853530680784
tex = "hola"
print(id(tex))
tex = "hola2"
print(id(tex))

# mutable, las listas son mutables al momento de agregar/quitar elementos
l = [1, 2, 3]
print(l, id(l))  # [1, 2, 3] 1818665703104
l.append(5)
print(l, id(l))  # [1, 2, 3, 5] 1818665703104

# strings
HELLO = "hola"
WORLD = "mundo"
text = f"{HELLO} {2+3} {WORLD}"
print(text[-1])
print(text[:len(text)-1])
print(text[1:len(text)-1])
print(text.title())
print(text.upper())  # lower, find, replace, strip(trim)
print("mundo" in text)  # True

# type conversion
X = 10
print(int(X))
print(float(X))
print(bool(X))  # Falsy: "", 0, 0.0, 0j, None, False, [], (), {}, set(), range(0)

# conditionals
if X > 10:
    print("High")
elif X > 5:
    print("Mid")
elif X > 2:
    print("Low")
else:
    pass  # si un if requiere quedarse vacio, usar "pass" keyword

# logical operators
NAME = " "
if not NAME.strip():
    print("Empty name")
AGE = 22
# cuasi-between
if 18 <= AGE < 35:  # same as: if age >= 18 and age < 35:
    print("young adult")

# ternary operator
MESSAGE = "OK" if AGE == 22 else "Not OK"
print(MESSAGE)

# for-loops
NAME = "Eder"
for X in NAME:  # los strings son iterables
    print(X)

for X in [1, 2, 3]:
    print(X)

for X in range(5):  # range es una built-in func que crea rangos
    print(X)

# for..else
for X in [1, 2, 3, 4]:
    if X == 5:
        print("found")
        break
else:  # else runs when "for" was not broken, similar to use a inner flag
    print("not found")

# while-loop
ANSWER = 5
GUESS = 0
while ANSWER != GUESS:
    GUESS += 1

# functions


def increment(number: int, by: int) -> int:
    """ increment a number

    Args:
        number (int): base number
        by (int): multiplier

    Returns:
        int: base number * multiplier
    """
    return number * by


def multy(*listy: int) -> int:  # *args
    """_summary_

    Returns:
        int: _description_
    """
    total = 1
    for i in listy:
        total *= i
    return total


print(multy(3, 3, 3))


def save_user(**dict_of_user: int):  # dictionary como parametro
    """_summary_

    Args:
        dict_of_user (dict(int)): dictionary of users
    """
    print(dict_of_user)


def save_user2(list_of_users: dict[int, str]):  # dictionary como parametro
    """_summary_

    Args:
        list_of_users (_type_): _description_
    """

    print(list_of_users)


save_user(id="1234", name="Eder")

# var scope: local, global but NOT block scope
MESSAGE = "Hello"


def greet():
    """greet function"""
    # global message, use message global variable into greet() function
    # pylint detects similar names btw global and local variables
    message = "Happy birthday"
    print(message)


greet()
print(MESSAGE)

# fizzBuzz algo


def fizz_buzz(input_value: int) -> str:
    """_summary_

    Args:
        input_value (int): _description_

    Returns:
        str: _description_
    """
    if input_value % 3 == 0 and input_value % 5 == 0:
        return "FizzBuzz"
    elif input_value % 3 == 0:
        return "Fizz"
    elif input_value % 5 == 0:
        return "Buzz"
    else:
        return "-"


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(2))
