"""_summary_"""
from abc import ABC, abstractmethod


class Animal:
    """______"""

    def __init__(self):
        self.age = 1

    @abstractmethod
    def eat(self):
        """ eat """
        print("eating")

    @abstractmethod
    def walk(self):
        """ walk """


class Mammal(Animal):
    """ ____ """

    def __init__(self):
        super().__init__()
        self.weight = 2

    def eat(self):
        """ eat """
        print("eating")

    def walk(self):
        super().walk()
        print("Mammal walking")
