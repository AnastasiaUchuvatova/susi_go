from Card import Card
from Cardlist import Deck
from Player import Player


class Game:
    # для 3 игроков
    DEFAULT_HAND_SIZE = 9
    PLAYER_SIZE = 3


    class State:

        PLAY_CARD = 'PLAY_CARD'  # начало раунда
        END = 'END'  # игра закончена

    def __init__(self):
        self.player = [''] * self.PLAYER_SIZE
        self.list_index = None
        self.state = None
        self.deck = None

    @staticmethod
    def create_deck():
        all_cards = Deck([Card('яйцо_нигири')])
        for i in range(4):
            all_cards.add(Card('яйцо_нигири'))
        for i in range(14):
            all_cards.add(Card('темпура'))
            all_cards.add(Card('сасими'))
            all_cards.add(Card('клёцки'))
        for i in range(10):
            all_cards.add(Card('пудинг'))
        for i in range(21):
            all_cards.add(Card('суси_ролл'))
        for i in range(10):
            all_cards.add(Card('лосось_нигири'))
        for i in range(5):
            all_cards.add(Card('кальмар_нигири'))
        return all_cards

    @staticmethod
    def create(player_names, hand_size = 9):
        game = Game()
        game.deck = Game.create_deck()
        game.deck.shuffle()
        i = 0
        for name in player_names:
            game.player[i] = Player(name)
            i += 1
        game.list_index = 0
        game.player_size = i - 1
        game.decks = [Deck([Card(' ')])] * 3
        for i in range(3):
            d = game.deck.draw(hand_size)
            game.decks[i] = Deck(d)
        game.state = Game.State.PLAY_CARD

        return game


    def next_cardlist(self):
        self.list_index = (self.list_index + 1) % self.PLAYER_SIZE

    def model_update(self, decks):
        # начало раунда
        if self.state == Game.State.PLAY_CARD:
            for i in range(self.PLAYER_SIZE):
                deck = decks[(self.list_index + i) % self.PLAYER_SIZE]
                self.player[i].take_card(deck.draw(1))
            if len(self.decks[0]) == 0:
                self.state = Game.State.END



    def model_update_loop(self, decks):
        while self.state != Game.State.END:
            self.model_update(decks)
            print(self.player[0].name, self.player[0].hand)
            print(self.player[1].name, self.player[1].hand)
            print(self.player[2].name, self.player[2].hand)


    def congratulation_winner(self):
        p = self.player[0].hand.points()
        name = self.player[0].name
        if self.player[1].hand.points() > p:
            name = self.player[1].name
        if self.player[2].hand.points() > p:
            name = self.player[2].name
        print(f'Игрок {name} победил!')


app = Game.create(['Alisa', 'Bob', 'Charly'])
app.model_update_loop(app.decks)