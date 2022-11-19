import random
from Card import Card


class Deck():
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def __repr__(self):
        return ' '.join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def add(self, card: Card):
        """ Добавить карту в КОНЕЦ списка. """
        self.cards.append(card)

    def draw(self, size: int = 1) -> list[Card]:
        """Возвращает или список карт длины size, или одну карту, если size=1.
        Эти карты удаляются из колоды.
        """

        out = self.cards[:size]
        self.cards = self.cards[size:]
        if size == 1:
            out = out[0]
        return out

    def shuffle(self) -> None:
        """Перемешивает колоду"""
        random.shuffle(self.cards)
