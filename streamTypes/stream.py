"""_summary_
    """
from abc import ABC, abstractmethod


class Stream(ABC):
    """ Stream """

    def __init__(self) -> None:
        pass

    def open(self):
        """_summary_"""

    def close(self):
        """_summary_"""

    @abstractmethod
    def read(self):
        """_summary_"""


class InvalidOperationError(Exception):
    """ InvalidOperationError """
