import random

number = random.randint(1, 100)
attempts = 0

name = input("Привет! Как тебя зовут? ")

while True:
    guess = int(input("Угадай число от 1 до 100: "))
    attempts += 1
    
    if guess < number:
        print("the number is bigger, try again ")
    elif guess > number:
        print("the number is smaller , try again")
    else:
        print("Congratulations, {}! You guessed the number in {} attempts!".format(name, attempts))
        break

with open('C:\\Users\\User\\Desktop\\репозиторий\\2\\python\\Middle\\game.txt', 'a') as f:
    f.write("{} guessed the number {} in {} attempts! good job!\n".format(name, number, attempts))