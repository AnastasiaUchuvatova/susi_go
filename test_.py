from Card import Card
from Hand import Hand


def test_Card_repr():
    ca = Card('лосось нигири')
    assert (repr(ca) == 'лосось нигири')


def test_Hand_add():
    ca = Card('лосось нигири')
    mas = Hand([ca])
    assert (repr(mas) == 'лосось нигири')
    assert (len(mas) == 1)
    ca1 = Card('яйцо нигири')
    mas.add(ca1)
    assert (repr(mas) == 'лосось нигири яйцо нигири')
    assert (len(mas) == 2)

def test_Hand_points():
    mas = Hand([Card('лосось нигири'), Card('темпура'), Card('сасими'), Card('клёцки'), Card('пудинг'),Card('суси ролл'),Card('лосось нигири'),Card('кальмар нигири'),Card('яйцо нигири') ])
    mas1 = Hand([Card('темпура'), Card('темпура'), Card('сасими'), Card('клёцки'), Card('лосось нигири'),Card('яйцо нигири'),Card('лосось нигири'),Card('кальмар нигири'),Card('кальмар нигири') ])
    mas2 = Hand([Card('темпура'), Card('лосось нигири'), Card('сасими'), Card('кальмар нигири'), Card('темпура'),Card('яйцо нигири'),Card('лосось нигири'),Card('кальмар нигири'),Card('сасими') ])
    assert (mas.points() == 9)
    assert (mas1.points() == 17)
    assert (mas2.points() == 16)
