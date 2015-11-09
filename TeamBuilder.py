###################################################################################################
# GUI imports
###################################################################################################


import Tkinter as tk


###################################################################################################
# imports from my files
###################################################################################################


from Card import *
from Team import *


###################################################################################################
# static functions
###################################################################################################


# returns true if a string represents an int
def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


###################################################################################################
# Main display window
###################################################################################################


class Display(tk.Frame):

    card_dictionary = {}  # stores all of the cards buttons represented by those cards
    user_team = Team([])  # stores the users current team
    teams = []            # stores a list of all of the teams
    total = 0.0           # used to calculate the percentage that a certain
    label_width = 250

    def __init__(self, parent, card_file, team_file):
        tk.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Team Builder")
        self.pack(fill=tk.BOTH, expand=1)
        w = tk.Label(self,
                     background="purple",
                     width=self.label_width,
                     height=self.parent.winfo_screenheight()
        )
        w.place(y=0, x=(self.parent.winfo_screenwidth()-self.label_width))
        self.gen_teams(team_file)
        self.gen_card_dictionary(card_file)
        self.display_buttons()
        self.pack(fill=tk.BOTH)

    # takes in a file name and uses this to construct a dictionary of all of the cards
    # and creates all of the buttons
    def gen_card_dictionary(self, cards_file):
        card_date_base = open(cards_file, "r")
        card_data = card_date_base.read().split("\n")
        i = 0
        for line in card_data:
            description = line.split(",")
            name = description[0].lower()
            rarity = description[1].lower()
            self.card_dictionary[name] = Card(name, 0)
            self.card_dictionary[name].rarity = rarity
            self.card_dictionary[name].button = tk.Button(self, text=name,
                                                       command=lambda name=name:
                                                       self.add_card(name))
            if rarity == "common":
                self.card_dictionary[name].button.configure(bg="grey")
            elif rarity == "uncommon":
                self.card_dictionary[name].button.configure(bg="green")
            elif rarity == "rare":
                self.card_dictionary[name].button.configure(bg="yellow")
            elif rarity == "super rare":
                self.card_dictionary[name].button.configure(bg="red")
            elif rarity == "promo":
                self.card_dictionary[name].button.configure(bg="blue")
            self.card_dictionary[name].button.place(y=i)
            i += 30
        card_date_base.close()

    # takes in a file name and then uses it to construct a list of all known teams
    def gen_teams(self, teams_file):
        team_data_base = open(teams_file, "r")
        team_data = team_data_base.read().split("\n")
        team = Team([])
        for line in team_data:
            if line == "":
                self.teams += [team]
                team = Team([])
            elif is_int(line):
                team.wins = int(line)
            else:
                card = Card(line.lower(), 0)
                team.cards += [card]
        team_data_base.close()

    # Loops over all of the buttons and displays them in their new positions
    def display_buttons(self):
        for key in self.card_dictionary.keys():
            card = self.card_dictionary[key]
            if not self.user_team.contains(card):
                if self.total == 0:
                    card.button.place(x=0)
                else:
                    x=(card.priority/self.total)*(self.parent.winfo_screenwidth()-self.label_width)
                    card.button.place(x=x)
            else:
                card.button.place(x=self.parent.winfo_screenwidth() - card.button.winfo_width())

    # Takes in the name of a card, adds it to the user's team and then calculates the new priority
    # values before updating the display
    def add_card(self, name):
        user_card = self.card_dictionary[name]
        for team in self.teams:
            if team.contains(user_card):
                self.total += 10
                for card in team.cards:
                    try:
                        self.card_dictionary[card.name].priority += team.wins
                    except:
                        pass
        self.user_team.cards += [user_card]
        user_card.button.configure(command=lambda name=name: self.remove_card(name))
        self.display_buttons()

    # Takes in the name of a card removes it from the user's team and then calculates the new
    # priority values before updating the display

    def remove_card(self, name):
        user_card = self.card_dictionary[name]
        for team in self.teams:
            if team.contains(user_card):
                self.total -= 10
                for card in team.cards:
                    try:
                        self.card_dictionary[card.name].priority -= team.wins
                    except LookupError:
                        pass
        self.user_team.cards.remove(user_card)
        user_card.button.configure(command=lambda name=name: self.add_card(name))
        self.display_buttons()


###################################################################################################
# runs the main program, generating the window
###################################################################################################


def main():
    root = tk.Tk()
    root.geometry("250x150+300+300")
    ex = Display(root, "cards.txt", "teams.txt")
    root.mainloop()
    return 0

if __name__ == "__main__":
    main()

