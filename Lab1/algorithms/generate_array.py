#generate_array.py
from random import randint

def generate_array(n):
    A = []
    for i in range(n):
        A.append(randint(0, 100000000000))
    
    return A