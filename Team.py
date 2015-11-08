from Card import *

"""
    stores data related to a team of dice master cards

"""
class Team:

    cards = []

    def __init__(self, cards):
        self.cards = cards

    def contains(self, card):
        for i in self.cards:
            if card.equals(i):
                return True
        return False
