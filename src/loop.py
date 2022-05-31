import time
import game


def play_games(hands: int=100000):
    hands = 0
    wins = 0
    payout = 0

    tracker = (hands, wins, payout)
    for i in range(hands):
        results = play_hand()
        tracker = [sum(x) for x in zip(tracker, results)]

    return tracker

