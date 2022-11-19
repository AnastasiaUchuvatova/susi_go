from Card import Card
from Cardlist import Cardlist, Deck


class Round:
    # для 3 игроков
    DEFAULT_HAND_SIZE = 9
    PLAYER_SIZE = 3

    PLAY_CARD = 'PLAY_CARD'     # начало хода игрока
    NEXT_PLAYER = 'NEXT_PLAYER' # ход игрока закончен
    END = 'END'                 # раунд закончен

    def __init__(self):
        self.players = None
        self.player_index = None
        self.state = None

    @staticmethod
    def create_deck():
        all_cards = Deck([Card('яйцо нигири')])
        for i in range(4):
            all_cards.add(Card('яйцо нигири'))
        for i in range(14):
            all_cards.add(Card('темпура'))
            all_cards.add(Card('сасими'))
            all_cards.add(Card('клёцки'))
        for i in range(10):
            all_cards.add(Card('пудинг'))
        for i in range(21):
            all_cards.add(Card('суси ролл'))
        for i in range(10):
            all_cards.add(Card('лосось нигири'))
        for i in range(5):
            all_cards.add(Card('кальмар нигири'))
        return all_cards

    @staticmethod
    def create_round(player_names: list[str], hand_size: int = DEFAULT_HAND_SIZE):
        """Подготовка к игре:
        Создается 3 массива из 9 карт
        """
        round = Round()

        return round

    def next_cardlist(self):
        self.player_index = (self.player_index + 1) % self.PLAYER_SIZE

    def turn(self):
        pass

a = Round.create_deck()
a.shuffle()
print(repr(a))
