import pytest

from core.card import Card
from core.hand import Hand
from core.deck import Deck

@pytest.fixture
def rand_hand():
    return Hand(Deck(13,5).cards[1:5]) #Produce random hand of five cards

@pytest.fixture
def test_hand():
    return Hand([Card(9,2), Card(3,3), Card(0,0), Card(4,0), Card(3,1)])

@pytest.fixture
def test_card():
    return Card(1,4) #Wild Two

def test_add_size(rand_hand: Hand, test_card: Card):
    #Confirm that += operation on Hand increases size by one.
    initial_size = len(rand_hand.cards)
    rand_hand += test_card
    assert len(rand_hand.cards) == initial_size + 1
    
def test_suit_count(test_hand: Hand):
    assert test_hand % 0 == 2

#Testing pair counting

@pytest.mark.parametrize("p_hand, points", [
    (Hand(Deck(13, 1).cards[0:5]), 0), #Hand with no pairs scores 0 points from pairs
    (Hand([Card(1,4), Card(3,3), Card(1,3), Card(2,1), Card(10,1)]), 2), #Hand with one pair scores 2 points
    (Hand([Card(1,4), Card(2,3), Card(1,3), Card(2,1), Card(10,1)]), 4), #Hand with two pairs scores 4 points
    (Hand([Card(1,4), Card(3,3), Card(1,3), Card(1,1), Card(10,1)]), 6), #Hand with three-of-a-kind scores 6 points
    (Hand([Card(1,4), Card(1,3), Card(1,0), Card(1,1), Card(1,4)]), 20), #Hand with five-of-a-kind scores 20 points
])
   
def test_pairs(p_hand: Hand, points: int):
    assert p_hand.pair_points() == points
     
#Testing fifteen counting
@pytest.mark.parametrize("f_hand, points", [
    (Hand(Deck(2, 5).cards[0:5]), 0), #Five cards from this deck can add to at most 10 (only ranks are A and 2). Zero fifteen points expected.
    (Hand([Card(0,4), Card(5,3), Card(10,3), Card(8,1), Card(10,1)]), 2), #Hand of A, 6, J, 9, J has one possible 15; scores 2 points.
    (Hand([Card(5,4), Card(4,3), Card(12,3), Card(2,1), Card(10,1)]), 4), #Hand with 6, 5, K, 3, J has two possible 15 combinations; scores 4 points.
    (Hand([Card(8,4), Card(3,3), Card(8,3), Card(1,1), Card(5,1)]), 8), #Hand with 9, 4, 9, 2, 6 has four possible 15 combinations; scores 8 points.
])

def test_fifteen_points(f_hand: Hand, points: int):
    assert f_hand.fifteen_points() == points
    
#Testing fifteen counting
@pytest.mark.parametrize("flush_hand, points", [
    (Hand(Deck(1, 13).cards[0:5]), 0), #This deck has only one rank; each card has a different suit. Flushes should be impossible; scores 0 from flushes.
    (Hand([Card(0,4), Card(5,3), Card(10,3), Card(8,1), Card(10,1)]), 0), #Maximum number of same suit cards is 2; scores 0 from flushes.
    (Hand([Card(5,3), Card(4,3), Card(12,3), Card(2,1), Card(10,3)]), 4), #Hand with four same-suited cards. Scores 4 from flushes.
    (Hand([Card(8,3), Card(3,3), Card(9,3), Card(1,3), Card(5,3)]), 5), #Hand with all cards the same suit. Scores 5 from flushes.
])
  
#Testing flush_points
def test_flush_points(flush_hand: Hand, points: int):
    assert flush_hand.flush_points() == points
    
#Testing eyes_points
@pytest.mark.parametrize("eyes_hand, cut, points", [
    (Hand(Deck(11, 1).cards[0:4]), Card(11,0), 0), #This deck has only one suit, with ranks A-J. Cut card is Q with same suit. Since there is no king/eye anywhere in cardset, eyes is impossible; scores 0.
    (Hand([Card(0,4), Card(5,3), Card(10,3), Card(8,1)]), Card(12,1), 0), #Cut card is king/eye, and has card matching suit in hand. This should NOT score an eye point.
    (Hand([Card(5,3), Card(4,3), Card(12,3), Card(2,1)]), Card(10,3), 1), #Hand containing king/eye matching suit of cut card. Scores 1 from eyes.
])

def test_eyes_points(eyes_hand: Hand, cut: Card, points: int):
    assert eyes_hand.eyes_points(cut) == points

#Testing ring_points
@pytest.mark.parametrize("ring_hand, points", [
    (Hand(Deck(1, 5).cards), 5), #This deck has only one rank; each card has a different suit, so guaranteed to form ring.
    (Hand([Card(0,4), Card(5,2), Card(10,3), Card(8,0), Card(10,1)]), 5), #This hand has multiple Jacks, but all different suits. It forms a ring.
    (Hand([Card(5,3), Card(4,1), Card(12,3), Card(2,1), Card(10,2)]), 0), #Hand with two pairs of same-suited cards. Does NOT form a ring.
])

def test_ring_points(ring_hand: Hand, points: int):
    assert ring_hand.ring_points() == points