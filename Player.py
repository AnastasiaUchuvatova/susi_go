from Hand import Hand


class Player:
    def __init__(self, name: list[str]):
        self.name = name
        self.hand = Hand('')

    def __repr__(self):
        return f'{self.name}: {self.hand}'

    def take_card(self, card):
        self.hand.add(card)
