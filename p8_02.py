class giraffes:
    def __init__(self, spots, who):
        self.giraffes_spots = spots
        self.giraffes_who = who
oz = giraffes(100, "son")
ge = giraffes(150, "mother")
gf = giraffes(200, "father")
print(oz.giraffes_spots, oz.giraffes_who)
