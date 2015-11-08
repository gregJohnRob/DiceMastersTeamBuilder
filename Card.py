from ttk import Button
"""
    stores all data related to a dice masters card
"""
class Card:

    name = ""
    rarity = ""
    priority = 0
    button = Button()

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


    def display(self):
        print self.name

    def equals(self, card):
        return self.name == card.name
