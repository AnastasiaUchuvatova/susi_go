from Card import Card
from Cardlist import Deck
from Hand import Hand



def test_Card_repr():
    ca = Card('лосось_нигири')
    assert (repr(ca) == 'лосось_нигири')

def test_Hand_add():
    ca = Card('лосось_нигири')
    mas = Hand([ca])
    assert (repr(mas) == ['лосось_нигири'])
    ca1 = Card('яйцо_нигири')
    mas.add(ca1)
    assert (repr(mas) == 'лосось_нигири яйцо_нигири')


def test_Hand_points():
    mas = Hand([Card('лосось_нигири'), Card('темпура'), Card('сасими'), Card('клёцки'), Card('пудинг'),Card('суси_ролл'),Card('лосось_нигири'),Card('кальмар_нигири'),Card('яйцо_нигири') ])
    mas1 = Hand([Card('темпура'), Card('темпура'), Card('сасими'), Card('клёцки'), Card('лосось_нигири'),Card('яйцо_нигири'),Card('лосось_нигири'),Card('кальмар_нигири'),Card('кальмар_нигири') ])
    mas2 = Hand([Card('темпура'), Card('лосось_нигири'), Card('сасими'), Card('кальмар_нигири'), Card('темпура'),Card('яйцо_нигири'),Card('лосось_нигири'),Card('кальмар_нигири'),Card('сасими') ])
    assert (mas.points() == 9)
    assert (mas1.points() == 17)
    assert (mas2.points() == 16)

def test_Cardlist_Deck_draw():
    a = Deck(['темпура', 'сасими', 'клёцки'])
    assert(a.draw(2) == ['темпура', 'сасими'])

def test_Cardlist_Deck_shuffle():
    a = Deck(['темпура', 'сасими', 'клёцки'])
    assert (a.shuffle() != 'темпура сасими клёцки')