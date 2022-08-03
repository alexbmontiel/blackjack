"""
This module contains the code to run many games of blackjack and
track the results.
"""
import sys
from joblib import Parallel, delayed
from multiprocessing import cpu_count

import src.blackjack.game as game


def main(
    n_hands: int = 1000,
    parallel: bool = False,
    verbose: bool = False
):
    if parallel is True:
        hands, wins, payout, loss = play_games_parallel(n_hands, verbose)
    else:
        hands, wins, payout, loss = play_games(n_hands, verbose)

    losses = hands - wins
    ties = n_hands - hands
    net_pay = payout - loss
    avg_win = payout / wins
    avg_loss = loss / losses
    win_rate = wins / n_hands
    loss_rate = losses / n_hands

    house_edge = round((loss_rate * avg_loss - win_rate * avg_win) * 100, 2)

    # Enable calls to print
    sys.stdout = sys.__stdout__

    # Make printed bar dynamic length (yes, really)
    len_n_hands = len(str(n_hands))

    print(f"Results of playing {n_hands} games:")
    print("=" * (26 + len_n_hands))
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")
    print(f"Payout: ${net_pay}")
    print(f"House edge: {house_edge}%")


def play_games(n_hands: int, verbose: bool):
    """Play blackjack for a given number of hands
    and return raw results.

    Uses a simple, non-parallelized, loop.

    Args:
      n_hands (int): Number of hands to play

    Returns:
      hands (int): Number of non-tie hands played
      wins (int): Number of player wins
      payout (float): $ Payout from wins
      loss (float): $ Payout from losses
    """
    # Initialize results
    hands = 0
    wins = 0
    payout = 0
    loss = 0

    tracker = (hands, wins, payout, loss)

    # Play for {hands} loops
    for i in range(n_hands):
        results = game.play_hand(verbose)
        # Add results to tally
        tracker = [sum(x) for x in zip(tracker, results)]

    hands = tracker[0]
    wins = tracker[1]
    payout = tracker[2]
    loss = tracker[3]

    return hands, wins, payout, loss


def play_games_parallel(n_hands: int, verbose: bool):
    """Play blackjack for a given number of hands
    and return raw results.

    Uses a parallelized queue, using all available cores.

    Args:
      n_hands (int): Number of hands to play

    Returns:
      hands (int): Number of non-tie hands played
      wins (int): Number of player wins
      payout (float): $ Payout from wins
      loss (float): $ Loss from losses
    """
    cpus = cpu_count()
    tally = Parallel(
        n_jobs=cpus)(delayed(game.play_hand)(verbose) for i in range(n_hands)
    )

    hands = sum([i[0] for i in tally])
    wins = sum([i[1] for i in tally])
    payout = sum([i[2] for i in tally])
    loss = sum([i[3] for i in tally])

    return hands, wins, payout, loss
