from time import time
from time import ctime


class MyStr(str):
    """Class str"""

    def __new__(cls, value: str, author: str):
        """create new instance"""
        instance = super().__new__(cls, value)
        instance.author = author.capitalize()
        instance.time = ctime(time())
        return instance


class Archive:
    """Save old value"""
    _instance = None

    def __init__(self, num: int, val: str):
        """Add new num and val"""
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        """Created new class with lists for nums and vals."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.number = []
            cls._instance.value = []
        else:
            cls._instance.number.append(cls._instance.num)
            cls._instance.value.append(cls._instance.val)
        return cls._instance
