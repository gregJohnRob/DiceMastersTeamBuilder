from ttk import Button
from PIL import Image
"""
    stores all data related to a dice masters card
"""
class Card:

    name = ""
    rarity = ""
    priority = 0
    button = Button()
    file_name = ""

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def gen_file_name(self):
        name = self.name.split(": ")
        name[0] = name[0].replace(" ", "_")
        name[1] = name[1].replace(" ", "_")
        self.file_name = "images/" + name[0] + "/" + name[1] + ".jpg"

    def display(self):
        print self.name

    def equals(self, card):
        return self.name == card.name
