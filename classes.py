"""_summary_"""


class Point:
    """_summary_"""
    # atributo de clase, tmb puede ser modificado por instancias
    default_color = "Red"

    @classmethod
    def zero(cls):
        """_summary_"""
        return cls(0, 0)

        # constructor

    def __init__(self, x: int, y: int) -> None:
        # atributos de instancia
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        """_summary_

        Args:
            other (Point): object to compare

        Returns:
            _type_: bool
        """
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # método de instancia
    def draw(self):
        print(f"draw point {self.x}, {self.y}")


point = Point(1, 2)
point2 = Point(1, 2)
p = ""
print(point.x)
point.draw()
zero = Point.zero()
zero.draw()
print(isinstance(point, Point))
print(point)
print(point == point2)
print(point + point2)


class TagCloud:
    """_summary_"""

    def __init__(self):
        self.tags = {}

    def add(self, tag: str):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag: str):
        return self.tags.get(tag.lower(), 0)

    def __settitem__(self, key: str, value: int):
        self.tags[key.lower()] = value

    def __len__(self):
        return len(self.tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud.tags)
print(cloud["python"])
