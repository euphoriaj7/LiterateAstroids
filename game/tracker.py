
class Tracker():

    def __init__(self):
        self.health = 1
        self.score = 0

    def gethp(self):
        return self.health

    def minushp(self):
        self.health -= 1

    def resethp(self):
        self.health = 6

    def getscore(self):
        return self.score

    def addscore(self):
        self.score += 5

    def resetscore(self):
        self.score = 0