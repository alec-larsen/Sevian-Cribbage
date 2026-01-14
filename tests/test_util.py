import pytest
from core import util

@pytest.mark.parametrize("ranks, run, points", [
    ([3,0,1,2,9], [0,1,2,3], 4), #Count run of four contained within ranks exactly once. Should return 4.
    ([3,0,1,2,9], [9,10,11,12], 0), #run is not present in ranks, though ranks does contain a run. Should return 0.
    ([5,7,6,6,5], [5,6,7], 12), #Total of 4 runs of 5,6,7 in ranks. Should return 12 (4*3).
])

def test_specific_run_points(ranks: list[int], run: list[int], points: int):
    assert util.specific_run_points(ranks, run) == points