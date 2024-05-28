"""_summary_
    """
from streamTypes.stream import Stream


class FileStream(Stream):
    """ FileStream """

    def __init__(self) -> None:
        pass

    def open(self):
        print("Opened file")

    def close(self):
        print("Opened file")

    def read(self):
        print("Reading a file")
