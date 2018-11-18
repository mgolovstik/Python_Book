class LOOOOOOOL:
    pass
class pop(LOOOOOOOL):
    pass
class haha(LOOOOOOOL):
    pass
class animals(pop):
    def brethe(self):
        print('Дышит')
    def move(self):
        print('Двигается')
    def eat_food(self):
        print('Ест')
class mammals(animals):
    def feed_young_with_milk(self):
        print('Кормит детёнышей молоком')
class giraffes(mammals):
    def eat_leaves_from_trees(self):
        print('')
    def find_food(self):
        self.move()
        print('Я нашёл еду')
        self.eat_food()
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance(self):
        self.move()
        self.move()
        self.move()
        self.move()
        self.move()
        self.move()
        self.move()
        self.move()
redginald = giraffes()
redginald.dance()
