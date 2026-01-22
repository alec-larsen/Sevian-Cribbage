import pytest

from core.card import Card
from core.stack import Stack

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
    assert card.value == value

@pytest.mark.parametrize("card, other, equal", [
    (Card(3,1), Card(3,4), False), #Same rank, but not same suit; expect False.
    (Card(12,4), Card(11,4), False), #Same suit, but not same rank; expect False.
    (Card(9,0), Card(9,0), True), #Same rank and suit; expect True.
    (Card(7,1), Stack([Card(1,4), Card(5,2), Card(7,1), Card(12,4), Card(9,1)]).cards[2], True), #Third card in defined stack is the same as initial card; expect True.
])

def test_card_eq(card: Card, other: Card, equal: bool):
    assert (card == other) == equal
