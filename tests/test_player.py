from collections.abc import Callable
import random

import pytest

from core.deck import Deck
from core.hand import Hand
from core.player import Player

#Generate random hand of six cards and a crib of two cards from Sevian deck. Also randomly select an index from 0 to 5.
def player_crib_pair():
    tmp_deck = Deck(13,5)
    pl = Player("Anelace Foxglove")
    pl.hand = Hand(tmp_deck.cards[0:6])
    return (pl, Hand(tmp_deck.cards[6:8]), random.randint(0,5))

#Verify that player hand length is modified by throw_card
@pytest.mark.parametrize("pair_crib_factory", [
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
])

def test_throw_card_hand(pair_crib_factory: Callable[[], tuple[Player, Hand, int]]):
    pl, crib, i = pair_crib_factory()
    init_len = len(pl.hand) #Save initial size of player hand for comparison
    pl.throw_card(i, crib)
    assert len(pl.hand) == init_len - 1 #Player's hand should now have one less card than before.

#Verify that crib length is modified by throw_card
@pytest.mark.parametrize("pair_crib_factory", [
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
    player_crib_pair,
])

def test_throw_card_crib(pair_crib_factory: Callable[[], tuple[Player, Hand, int]]):
    pl, crib, i = pair_crib_factory()
    init_len = len(crib) #Save initial size of crib for comparison.
    pl.throw_card(i, crib)
    assert len(crib) == init_len + 1 #Crib should now contain one more card than before.
