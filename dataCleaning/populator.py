import os

# Directory where examples will be saved
OUTPUT_DIR = "python_oop_examples"

# List of 100 example code snippets (strings)
examples = [
    # 1
    '''class Dog:
    pass
''',
    # 2
    '''class Dog:
    def __init__(self, name):
        self.name = name
''',
    # 3
    '''class Dog:
    def bark(self):
        print("Woof!")
''',
    # 4
    '''class Dog:
    species = "Canis familiaris"
''',
    # 5
    '''class Dog:
    def __init__(self, name):
        self.name = name
''',
    # 6
    '''d = Dog("Buddy")
''',
    # 7
    '''print(d.name)
''',
    # 8
    '''class Animal:
    pass

class Dog(Animal):
    pass
''',
    # 9
    '''class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("Woof!")
''',
    # 10
    '''class A:
    pass

class B:
    pass

class C(A, B):
    pass
''',
    # 11
    '''class Dog:
    @classmethod
    def info(cls):
        print("Dogs are mammals.")
''',
    # 12
    '''class Math:
    @staticmethod
    def add(a, b):
        return a + b
''',
    # 13
    '''class Dog:
    def __init__(self, name):
        self.__name = name
''',
    # 14
    '''class Dog:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
''',
    # 15
    '''class Dog:
    def set_name(self, name):
        self.__name = name
''',
    # 16
    '''class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
''',
    # 17
    '''class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
''',
    # 18
    '''class Dog:
    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name
''',
    # 19
    '''class Dog:
    def __str__(self):
        return "Dog object"
''',
    # 20
    '''class Dog:
    def __repr__(self):
        return f"Dog({self.name})"
''',
    # 21
    '''class Dog:
    def __eq__(self, other):
        return self.name == other.name
''',
    # 22
    '''class Dog:
    def __len__(self):
        return 4
''',
    # 23
    '''class Dog:
    def __call__(self):
        print("Dog called!")
''',
    # 24
    '''class Dog:
    def __del__(self):
        print("Dog deleted")
''',
    # 25
    '''from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
''',
    # 26
    '''class Dog(Animal):
    def speak(self):
        print("Woof!")
''',
    # 27
    '''def animal_sound(animal):
    animal.speak()
''',
    # 28
    '''class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
''',
    # 29
    '''class Wheel:
    pass

class Car:
    def __init__(self, wheel):
        self.wheel = wheel
''',
    # 30
    '''class Dog:
    species = "Canis familiaris"
    def __init__(self, name):
        self.name = name
''',
    # 31
    '''class Person:
    def set_name(self, name):
        self.name = name
        return self
''',
    # 32
    '''class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
''',
    # 33
    '''class Dog:
    @classmethod
    def create(cls, name):
        return cls(name)
''',
    # 34
    '''print(issubclass(Dog, Animal))
''',
    # 35
    '''print(isinstance(d, Dog))
''',
    # 36
    '''class MyError(Exception):
    pass
''',
    # 37
    '''class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
''',
    # 38
    '''class Math:
    def add(self, a, b=0):
        return a + b
''',
    # 39
    '''class Vector:
    def __add__(self, other):
        return Vector()
''',
    # 40
    '''class Counter:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        self.n += 1
        if self.n > 5:
            raise StopIteration
        return self.n
''',
    # 41
    '''class MyList:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return iter(self.data)
''',
    # 42
    '''class FileOpener:
    def __enter__(self):
        self.file = open('file.txt')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
''',
    # 43
    '''class MyDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Before")
        return self.func(*args, **kwargs)
''',
    # 44
    '''class Date:
    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)
''',
    # 45
    '''class Math:
    @staticmethod
    def square(x):
        return x * x
''',
    # 46
    '''class Test:
    def __init__(self):
        self.__private = 42
''',
    # 47
    '''class Dog:
    """A simple dog class."""
''',
    # 48
    '''class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
''',
    # 49
    '''class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        super().hello()
        print("Hello from B")
''',
    # 50
    '''class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
''',
    # 51
    '''class Outer:
    class Inner:
        pass
''',
    # 52
    '''class Config:
    DEBUG = True
    VERSION = "1.0"
''',
    # 53
    '''class Point:
    __slots__ = ['x', 'y']
''',
    # 54
    '''class Dynamic:
    pass

d = Dynamic()
d.new_attr = 5
''',
    # 55
    '''class Dog:
    pass

d = Dog()
print(type(d) == Dog)
''',
    # 56
    '''class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
''',
    # 57
    '''class Person:
    def __init__(self, name):
        self.__name = name
''',
    # 58
    '''class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

def animal_sound(animal):
    animal.speak()
''',
    # 59
    '''class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking!")
''',
    # 60
    '''class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
''',
    # 61
    '''class Reverse:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return reversed(self.data)
''',
    # 62
    '''class MyList:
    def __init__(self):
        self.data = []
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
''',
    # 63
    '''class Managed:
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
''',
    # 64
    '''class Person:
    def __hash__(self):
        return hash(self.name)
''',
    # 65
    '''class Person:
    def __lt__(self, other):
        return self.age < other.age
''',
    # 66
    '''class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1
        return self.current - 1
''',
    # 67
    '''class Utility:
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("Cannot instantiate Utility class")
''',
    # 68
    '''class Decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Decorated!")
        return self.func(*args, **kwargs)
''',
    # 69
    '''class Test:
    def __init__(self):
        self.x = 1
print(Test().__dict__)
''',
    # 70
    '''class Test:
    __slots__ = ['x']
''',
    # 71
    '''class Person:
    def __init__(self, name="John"):
        self.name = name
''',
    # 72
    '''class Person:
    def __init__(self, *args):
        self.data = args
''',
    # 73
    '''class Person:
    def __init__(self, **kwargs):
        self.data = kwargs
''',
    # 74
    '''class Person:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
''',
    # 75
    '''class Final(type):
    def __new__(mcs, name, bases, namespace):
        for base in bases:
            if isinstance(base, Final):
                raise TypeError("Cannot subclass final class")
        return super().__new__(mcs, name, bases, namespace)

class Base(metaclass=Final):
    pass
''',
    # 76
    '''class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['id'] = 1
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
''',
    # 77
    '''class MyClass:
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)
''',
    # 78
    '''class MyClass:
    def __init__(self):
        print("Initializing instance")
''',
    # 79
    '''class MyClass:
    @classmethod
    def hello(cls):
        print("Hello from class")
''',
    # 80
    '''class MyClass:
    @staticmethod
    def hello():
        print("Hello from static")
''',
    # 81
    '''class MyClass:
    pass

class Sub(MyClass):
    pass

print(issubclass(Sub, MyClass))
''',
    # 82
    '''class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, MyClass))
''',
    # 83
    '''class Person:
    @classmethod
    def from_birth_year(cls, name, year):
        from datetime import date
        age = date.today().year - year
        return cls(name, age)
''',
    # 84
    '''class Math:
    @staticmethod
    def multiply(a, b):
        return a * b
''',
    # 85
    '''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        from datetime import date
        age = date.today().year - year
        return cls(name, age)
''',
    # 86
    '''class Person:
    def __str__(self):
        return f"Person: {self.name}"
''',
    # 87
    '''class Person:
    def __repr__(self):
        return f"Person({self.name!r})"
''',
    # 88
    '''class Person:
    def __eq__(self, other):
        return self.name == other.name
''',
    # 89
    '''class Person:
    def __hash__(self):
        return hash((self.name, self.age))
''',
    # 90
    '''class Person:
    def __lt__(self, other):
        return self.age < other.age
''',
    # 91
    '''class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
''',
    # 92
    '''class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1
        return self.current - 1
''',
    # 93
    '''class MyList:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]
''',
    # 94
    '''class MyList:
    def __init__(self, data):
        self.data = data
    def __setitem__(self, index, value):
        self.data[index] = value
''',
    # 95
    '''class MyList:
    def __init__(self, data):
        self.data = data
    def __delitem__(self, index):
        del self.data[index]
''',
    # 96
    '''class MyList:
    def __init__(self, data):
        self.data = data
    def __contains__(self, item):
        return item in self.data
''',
    # 97
    '''class MyList:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
''',
    # 98
    '''class Greeter:
    def __call__(self, name):
        print(f"Hello, {name}!")
''',
    # 99
    '''class Managed:
    def __enter__(self):
        print("Entering")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting")
''',
    # 100
    '''class Person:
    def __format__(self, format_spec):
        if format_spec == 'short':
            return self.name
        else:
            return f"{self.name} ({self.age})"
''',
]

def main():
    # Create output directory if not exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for i, code in enumerate(examples, start=1):
        filename = f"example_{i:03}.py"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Created {filepath}")

if __name__ == "__main__":
    main()
