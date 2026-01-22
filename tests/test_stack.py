import pytest
from core.card import Card
from core.stack import Stack

#Test total sum of values in stack (__pos__)
@pytest.mark.parametrize("sum_stack, value",[
    (Stack([Card(1,3), Card(6,2), Card(3,3)]), 13), #Stack containing 2, 7, and 4 should sum to 13
    (Stack([Card(0,3), Card(4,2), Card(9,3), Card(0,1)]), 17), #Stack containing A, 5, 10, and A should sum to 17
    (Stack([Card(12,3), Card(7,2), Card(8,3), Card(11,1), Card(10, 1)]), 47), #Stack containing K, 8, 9, Q, and J should sum to 47
])

def test_stack_sum(sum_stack: Stack, value: int):
    assert +sum_stack == value

#Test flush point calculation in stack (__invert__)
@pytest.mark.parametrize("flush_stack, points", [
    (Stack([Card(6,3), Card(3,3), Card(6,2)]), 0), #Stack with last two cards matching suit. Should return 0.
    (Stack([Card(1,3), Card(3,3), Card(6,3), Card(7,3), Card(4,1)]), 4), #Stack with last four cards matching suit. Should return 4.
    (Stack([Card(4,3), Card(1,3), Card(3,3), Card(6,3), Card(7,3)]), 5), #Stack with last five cards matching suit. Should return 5.
    (Stack([Card(4,3), Card(1,1), Card(3,3), Card(6,3), Card(7,3)]), 0), #Stack with four same-suit cards, but not consecutive. Should return 0.
    (Stack([Card(4,2), Card(1,3), Card(3,3), Card(6,3), Card(7,3)]), 0), #Stack with four same-suit cards, consecutive but not at top of stack. Should return 0.
])

def test_stack_flush(flush_stack: Stack, points: int):
    assert ~flush_stack == points

#Test pair counting in stack.
@pytest.mark.parametrize("pair_stack, points", [
    (Stack([Card(1,2), Card(3,2), Card(4,2), Card(5,2)]), 0), #All different ranks (but all same suit); expect 0 pair points.
    (Stack([Card(5,3), Card(5,2), Card(1,0), Card(3,1)]), 2), #Pair at top of stack; expect 2 pair points.
    (Stack([Card(1,2), Card(4,3), Card(4,2), Card(6,2)]), 0), #Pair in middle of stack; expect 0 points as pairs in stacks only when they appear at the top of the stack.
    (Stack([Card(8,3), Card(8,1), Card(8,2), Card(1,2)]), 6), #Triple at top of stack; expect 6 pair points.
    (Stack([Card(5,4), Card(5,0), Card(5,1), Card(5,2)]), 12), #All four cards in stack are the same rank; expect 12 pair points.
])

def test_stack_pair(pair_stack: Stack, points: int):
    assert pair_stack.pairs() == points

#Test run counting in stack
@pytest.mark.parametrize("run_stack, points", [
    (Stack([Card(6,1), Card(4,3), Card(5,2), Card(1,2)]), 3), #Run of 3 at top of stack; expect 3 run points.
    (Stack([Card(4,0), Card(5,4), Card(5,1), Card(3,2)]), 0), #If this stack were a hand, it would score 6 run points. This, however should score 0, as 5,6,6,4 is NOT a single run, but two runs of three.
    (Stack([Card(10,2), Card(11,3), Card(9,2), Card(12,2)]), 4), #Run over entire stack; expect 4 run points.
    (Stack([Card(0,2), Card(7,2), Card(8,3), Card(9,1)]), 0), #Run of three, but NOT at top of stack; expect 0.
])

def test_stack_runs(run_stack: Stack, points: int):
    assert run_stack.runs() == points

#Test add_card
params = [
    (Stack([Card(4,1), Card(1,4), Card(3,1), Card(3,4)]), Card(3,2), True, Card(3,2)), #Initial stack sums to 15; attempting to add a 4 should return True.
    (Stack([Card(4,1), Card(7,4), Card(3,1), Card(3,4)]), Card(9,2), True, Card(9,2)), #Initial stack sums to 21; attempting to add a 10 leaves the stack at EXACTLY 31; should return True.
    (Stack([Card(5,1), Card(3,2), Card(3,1), Card(7,4)]), Card(9,2), False, Card(5,1)), #Initial stack sums to 22; attempting to add a 10 leaves the stack at 32; should return False.
]

#Verify that add_card correctly returns whether new_card can be added to the stack.
@pytest.mark.parametrize("add_stack, new_card, success, top_card", params)
def test_add_return(add_stack: Stack, new_card: Card, success: bool, top_card: Card): #pylint: disable=unused-argument
    assert add_stack.add_card(new_card) == success

#Verify that add_card properly updates stack, leaving added card on top if legal to add.
@pytest.mark.parametrize("add_stack, new_card, success, top_card", params)
def test_add_top(add_stack: Stack, new_card: Card, success: bool, top_card: Card): #pylint: disable=unused-argument
    copy_stack = add_stack #Circumvent restriction that parameters are immutable.
    copy_stack.add_card(new_card)
    assert copy_stack.cards[0] == top_card
