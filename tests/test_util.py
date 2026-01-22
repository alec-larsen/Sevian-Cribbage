import pytest
from core import util
from core.card import Card

@pytest.mark.parametrize("ranks, run, points", [
    ([3,0,1,2,9], [0,1,2,3], 4), #Count run of four contained within ranks exactly once. Should return 4.
    ([3,0,1,2,9], [9,10,11,12], 0), #run is not present in ranks, though ranks does contain a run. Should return 0.
    ([5,7,6,6,5], [5,6,7], 12), #Total of 4 runs of 5,6,7 in ranks. Should return 12 (4*3).
])

def test_specific_run_points(ranks: list[int], run: list[int], points: int):
    assert util.specific_run_points(ranks, run) == points

@pytest.mark.parametrize("cards, run_found", [
    ([Card(5,1),Card(6,2),Card(7,3),Card(8,1),Card(9,0)], True), #Ordered run; expect True
    ([Card(1,0),Card(3,0),Card(2,0),Card(0,0)], True), #Unordered run; expect True
    ([Card(2,0),Card(4,1),Card(6,3),Card(3,2)], False), #Contains run of 3, but all ranks do NOT for run; expect False.
    ([Card(3,1),Card(4,3),Card(2,4),Card(9,1)], False), #Contains run of 3 (at bottom if cards are derived from Stack), but all rnaks do NOT form run; expect False.
    ([Card(0,0),Card(10,1),Card(9,4),Card(11,3)], False), #Contains run of 3 (at top if cards are derived from Stack), but all rnaks do NOT form run; expect False.
])

def test_is_run(cards: list[Card], run_found: bool):
    assert util.is_run(cards) == run_found
