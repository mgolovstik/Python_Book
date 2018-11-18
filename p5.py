m = 0
found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1,53):
    if week == 4:
        m = m + 1
        print('Месяц %s = %s' % (m,coins))
        coins = 0
        week = 0
    coins = coins + magic_coins - stolen_coins
    print('Неделя %s = %s' % (week,coins))
