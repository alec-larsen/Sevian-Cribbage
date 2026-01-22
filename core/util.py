from .card import Card
#from .hand import Hand

def specific_run_points(ranks: list[int], run: list[int]) -> int:
    """
    Calculate specific points from runs with specific ranks.

    Args:
        ranks (list[int]): List of all ranks to check over. May contain duplicates.
        run (list[int]): Set of ranks to check for runs over.
        
    Returns:
        int: Number of points scored from runs containing the listed ranks in run.
    """
    #This will track the total number of runs with the ranks listed in run.
    n = 1
    for rank in run:
        #Check the number of occurences of rank in ranks. Multiple copies of the same rank have a multiplicative effect on the number of runs possible to form.
        n *= ranks.count(rank)

    #Total points scored is the length of the run we checked times the number of runs we were able to form.
    return n*len(run)

def is_run(cards: list[Card]) -> bool:
    """
    Check if cards score single run.

    Args:
        cards (list[Card]): cards to check for run
        
    Returns:
        bool: True if ALL cards form single run, otherwise False.
    """
    ranks = [card.rank for card in cards]
    i = min(ranks)

    for _ in range(len(cards)-1):
        if i+1 not in ranks:
            return False
        i += 1
    return True
