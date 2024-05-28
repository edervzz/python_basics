"""_summary_
    """
from typing import List, Optional


class Student:
    """_summary_
    """

    def __init__(self, name, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        """_summary_ Args: result (int): _description_ """
        self.grades.append(result)


eder = Student("Eder")
shei = Student("Sheila")
eder.take_exam(90)
print(eder.grades)
print(shei.grades)
