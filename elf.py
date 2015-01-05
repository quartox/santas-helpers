__author__="Jesse Lord"
__date__="January 1, 2015"

class elf:
    def __init__(self,ID):
        self.id = ID
        self.rating = 1.0
        self.restperiod = 0.0 # hours of rest before more work
        self.improve = 1.02 # improve rating during sanctioned hours
        self.decrease = 0.9 # decrease rating during unsanctioned hours
