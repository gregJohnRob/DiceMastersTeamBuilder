def main():
    card_date_base = open("cards.txt", "r")
    cards = card_date_base.read().split("\n")
    cards = list(set(cards))
    cards.sort()
    card_date_base.close()
    card_date_base = open("cards.txt", "w")
    for card in cards:
        card_date_base.write(card + "\n")
    return 0


if __name__ == "__main__":
    main()

# string == string