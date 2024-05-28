"""_summary_"""


class TagCloud:
    """_summary_"""

    def __init__(self):
        self.__tags = {}

    def add(self, tag: str):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag: str):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, key: str, value: int):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def __str__(self) -> str:
        return str(self.__tags)

    def __repr__(self) -> str:
        return (
            f"<TagCloud({self.__tags!r})>"
        )  # !r calls the __repr__ method of the thing.


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud.__dict__)  # diccionario con los atributos de la clase
print(cloud._TagCloud__tags)
cloud["python"] = 5  # __setitem__
print(cloud["python"])  # __getitem__
print(len(cloud))  # __len__
for item in cloud:  # __iter__
    print(item)

print(cloud)  # __str__

print(cloud.__repr__)


class Person:
    """___"""

    def __init__(self, name: str):
        self.__name = name

    def get_age(self) -> int:
        """___"""
        return self.__age

    def set_age(self, age: int) -> None:
        """___"""
        if (age < 1):
            raise ValueError("Age most be greater than zero.")
        self.__age = age

    age = property(get_age, set_age, "propiedad name")

    @property
    def name(self):
        "I am the 'name' property"
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


p = Person("eder")
p.age = 10
print(p.name)
