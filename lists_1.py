import random
list_1 = random.sample(range(10000), random.randint(50, 100))
list_2 = random.sample(range(10000), random.randint(50, 100))
new_list = [n for n in list_1 if n not in list_2] #новый список в которм числа (n) из первого списка которых нет во втором
print(new_list)