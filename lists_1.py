import random
list_1 = random.sample(range(10000), random.randint(50, 100))
list_2 = random.sample(range(10000), random.randint(50, 100))
new_list = [num for num in list_1 if num not in list_2] #новый список в которм числа из первого списка которых нет во втором
print(new_list)