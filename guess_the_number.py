import random

random_num = random.randint(0, 100)
history = []
guess = int(input("try to guess the number : \n"))

while guess != random_num:
    if random_num >= guess:
        guess = int(input("The number you are trying to guess is bigger\n"))
        history.append(guess)
        
    else:
        guess = int(input("The number you are trying to guess is lower\n"))
        history.append(guess)


print("Congrats you won in", len(history), "tries")

for tries in history:
    print('- ', tries)
