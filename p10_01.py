import random
num = random.randint(1,100)
while True:
    print('Угадай число от 1 до 100!')
    guess = input()
    i = int(guess)
    if i == num:
        print('ПРАВИЛЬНО!')
        break
    elif i < num:
        print('Число больше!')
    elif i > num:
        print('Число меньше!')
        
        
