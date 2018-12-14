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
print('Хотите продолжить?')
print('Угадать число от 1 до 1000!')
print('Если ДА пишите "1" а если НЕТ пишите "0"')
yn = input()
yn2 = int(yn)
if yn2 == 1:
    num = random.randint(100,1000)
    while True:
        print('Угадай число от 1 до 1000!')
        guess2 = input()
        i2 = int(guess2)
        if i == num2:
            print('ПРАВИЛЬНО!')
            break
        elif i < num:
            print('Число больше!')
        elif i > num:
            print('Число меньше!')
elif yn2 != 666 :
    print('ОКЕЙ')
elif yn2 == 666:
    print('Я ДЬЯВОЛ, Я УБЬЮ ТЕБЯ')
