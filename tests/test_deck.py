from core.card import Card
from core.deck import Deck
import pytest

@pytest.fixture
def test_deck():
    return Deck(13,5)

@pytest.fixture
def test_card():
    return Card(2,3) #Vixian Three

@pytest.fixture
def false_card():
    return Card(11,6) #This card does not exist in a deck with only five suits.

def test_card_in_deck(test_deck: Deck, test_card: Card):
    assert test_card in test_deck
    
def test_false_card_not_in_deck(test_deck: Deck, false_card: Card):
    assert false_card not in test_deck

def test_deck_length(test_deck: Deck):        
    assert len(test_deck.cards) == 65
    
def test_deck_contains_all_cards(test_deck: Deck):
    for i in range(13):
        for j in range(5):
            assert Card(i,j) in test_deck