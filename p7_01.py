def spaceship_building(c):
    t_c = 0
    for week in range(1,53):
        t_c = t_c + c
        print('НЕДЕЛЯ %s, БАНКИ: %s' % (week, t_c))
spaceship_building(2)
