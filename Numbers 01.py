import random

def magic():
    n= random.sample(range(10000), random.randint(5,100)) 
    X = random.randint(1, 1000) 
    a = sum(n)% X == 0
    print(a) 
magic()