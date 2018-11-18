class giraffes:
    def l_f_f(self):
        print('Левая нога впереди')
    def l_f_b(self):
        print('Левая нога позади')
    def r_f_f(self):
        print('Правая нога впереди')
    def r_f_b(self):
        print('Правая нога впереди')
    def dance_1(self):
        self.l_f_f()
        self.r_f_b()
        self.r_f_f()
        self.l_f_b()
    def dance_2(self):
        self.l_f_f()
        self.r_f_b()
        self.l_f_b()
        self.l_f_f()
        self.r_f_f()
        self.l_f_b()
        self.r_f_b()
lol = giraffes()
lol.dance_2()
        
