
class Tracker():

    def __init__(self):
        self.health = 6
        self.score = 0

    def checkhp(self):
        return self.health

    def minushp(self):
        self.health -= 1

    def resethp(self):
        self.health = 6

    def checkscore(self):
        return self.score

    def addscore(self):
        self.score
#reset score f