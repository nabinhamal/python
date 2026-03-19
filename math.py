
from random import random
import math

print(math.sqrt(16))

# import specific functions
from math import sqrt ,pi

print(sqrt(16))

# import all functions
from math import *

print(sqrt(16))


import random

number = random.randint(1, 10)
print(number)

choice = random.choice(["apple", "banana", "cherry"])
print(choice)


import datetime

today = datetime.date.today()
print(today)


import os

print(os.getcwd()) 

import json



person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(json.dumps(person))

