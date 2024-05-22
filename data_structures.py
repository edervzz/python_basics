"""_summary_"""
import sys
from collections import deque
from array import array

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
