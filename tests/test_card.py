import pytest

from core.card import Card

@pytest.mark.parametrize("card, value", [
    (Card(0,1),1),
    (Card(1,3),2),
    (Card(8,1),9),
    (Card(9,1),10),
    (Card(10,2),10),
    (Card(11,0),10),
    (Card(12,4),10),
])

def test_card_values(card: Card, value: int):
    assert(card.value == value)