""" anotaciones """
import sys
from collections import deque
from array import array

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

# type casting
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


# lists
matrix = [[0, 1], [3, 4]]
print(matrix, type(matrix))
letters: list[str] = ["a", "b", "c"]
zeros = [0] * 5  # crea una lista de 5 ceros
print(zeros)
combined = zeros + letters  # combine lists
print(combined, type(combined))
chars = list("Hola Mundo")  # create a list of chars
print(chars)
numbers = list(range(10))  # create a list from range
print(numbers)
print(numbers[::2])  # obtiene numero pares, cambiar por 3 para impares
print(numbers[::-1])  # reversa
first, second, third, four, five, six, seven, eight, nine, ten = numbers  # unpack list
first, second, *other = numbers  # unpack list, rest lead into "other" list

# two ways to get same tuple
chars = list("Hola Mundo")
for c in enumerate(chars):
    print(c[0], c[1])

for idx, c in enumerate(chars):
    print(idx, c)

# add to list
letters: list[int] = ["a", "b", "c", "e", "f"]
letters.append("d")
letters.insert(2, "-")

# remove from list
letters.pop()
letters.pop(2)
letters.remove("c")
del letters[0:3]
letters.clear()
# find items
if "a" in letters:  # guard
    letters.index("a")
letters.count("d")  # 0

# lambdas


def sort_item(item):
    """sort function"""
    return item[1]


prod_prices = [
    ("PR3", 12),
    ("PR1", 10),
    ("PR2", 7),
]
prod_prices.sort(key=sort_item)  # normal call
print(prod_prices)
prod_prices.sort(key=lambda item: item[1])  # lambda call
print(prod_prices)

# map function
prices = list(map(lambda item: item[1], prod_prices))
print(prices)

# filter function
filtered = filter(lambda item: item[1] >= 10, prod_prices)
print(list(filtered))

# list comprehensions
print("List Comprehensions")
prices = [item[1] for item in prod_prices]
print(prices)
filtered = [item for item in prod_prices if item[1] >= 10]
print(filtered)
# zip function, combina y crea tuplas de varias listas por posicion
print("Zip Function")
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))
# stack(LIFO), simulacion de una stack con listas
browsing = []
browsing.append(1)
browsing.append(2)
browsing.append(3)
while browsing:
    e = browsing.pop()
    print(e)
# queue(FIFO), usamos tipo deque es mucho mas performante al momento del pop(-1)
# esto es porque pop(-1) recorre todos los elementos una posición
# lo cual para muchos elementos seria poco performante
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

# tuple dos formas igual se tuplas
# read-only list
point = (1, 2, 3)
point = 1, 2, 3
print(point[0])
point = (1, 2, 3) + (4, 5)
point = (1, 2, 3) * 3
point = tuple("Hello World")
point = tuple([1, 2])
x, y = point
# swapping vars, aplica un unpack con una tuple
x = 10
y = 11
x, y = y, x

# array, este es mucho mas performante además que fuerza a solo usar un tipo
# aquí se definen los tipos https://docs.python.org/3/library/array.html
numbers = array("i", [1, 2, 3])
# set, lista de valores irrepetibles
list_of_numbers = [1, 1, 2, 3, 3]
first = set(list_of_numbers)
second = {1, 4, 5}
print(first)
print(second)
# tambien es posible hacer operaciones con sets
print(first | second, "combinacion")  # combinación
print(first & second, "interseccion")  # interseccion
print(first - second, "diferencia")  # diferencia
print(first ^ second, "XOR")  # XOR

# dictionary {k, v}
point = {"x": "hello", "y": "world"}
point = {1: "hello", 2: "world"}
# dos formas similares
point = {"x": 1, "y": 2}
point = dict(x="adsf", y="asdf")
point["z"] = 19
print(point)
if "H" in point:
    print(point)
print(point.get("h"))  # sino existe retorna None
# dos formas de validar la existencia de una key
if None is point.get("h"):
    print("not found h")
if "w" in point:
    del point["w"]
else:
    print("not found w")
# iterar dictionary
for p in point:
    print(p, point[p])

for key, value in point.items():  # unpack tuple
    print(key, value)

# dictionary comprehensions
values = {}
for x in range(5):
    values[x] = x*2
print(values)
values = {x: x*2 for x in range(5)}  # comprehensions
print(values)

# generator object, con el uso de comprehensions, crear valores durante la iteracion
# ahorrando espacio en memoria
# a diferencia con una lista que los creara al momento
values = (x*2 for x in range(10))
print(values)  # <generator object <genexpr>
for v in values:
    print(v)
print(sys.getsizeof(values))  # 208
values = [x*2 for x in range(10000)]  # 85176
print(sys.getsizeof(values))

# unpacking operator
numbers = [1, 2, 3]
print(*numbers)
# dos formas de crear listas haciendo uso de unpacking operator
numbers = list(range(5))
numbers = [*range(5)]
# unpacking rango y texto
numbers = [*range(5), " a ", *"Hello"]
print(numbers)
# unpacking dictionaties
first = {"x": 1}
second = {"y": 2}
combined = {**first, **second, "z": 30}
print(combined)

# ejercicio
sentence = "This is a common interview question"
chars = list(sentence)
counter_chars = dict({})

for e in chars:
    if e in counter_chars:
        counter_chars[e] += 1
    else:
        counter_chars[e] = 1

print([(k, v) for k, v in counter_chars.items()])

counter_sorter_chars = sorted(
    counter_chars.items(),
    key=lambda kv: kv[0],
    reverse=True
)

print(counter_sorter_chars)


def add(x, y):
    return x + y


nums = [15, 25]
print(add(*nums))
nums = {"x": 15, "y": 25}

for item, v in nums.items():
    print(item, v)

print(add(nums["x"], nums["y"]))
