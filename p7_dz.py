import sys
def moon_weight():
    print('Введите ваш вес')
    e = int(sys.stdin.readline())
    print('Введите ежегодный прирост веса')
    f = float(sys.stdin.readline())
    print('Введите кол. лет')
    g = int(sys.stdin.readline())
    d = e + f * g
    print('Ваш вес через %s лет: %s КГ' % (g,d))
moon_weight()
