from time import time
from time import ctime


class MyStr(str):
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author.capitalize()
        instance.time = ctime(time())
        return instance


class Archive:
    _instance = None

    def __init__(self, num: int, val: str):
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.number = []
            cls._instance.value = []
        else:
            cls._instance.number.append(cls._instance.num)
            cls._instance.value.append(cls._instance.val)
        return cls._instance
