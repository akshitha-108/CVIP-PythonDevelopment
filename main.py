import random
class RandomError(Exception):
    pass
try:
    num=random.random()
    if num < 0.1:
        raise RandomError
except RandomError as e:
    print("random as genersted")
else:
    print("%3f"%num)