"""
This module contains the code to actually play a hand of blackjack
and return the results.
"""
import src.blackjack as blackjack
import src.strategies as strategies
import src.checks as checks

import sys
import os


def play_hand(verbose: bool):
    """Play a hand of blackjack.

    Args:
      verbose (bool): Optionally suppress print statements
    """
    if verbose is False:
        sys.stdout = open(os.devnull, "w")

    player = blackjack.Hand()
    dealer = blackjack.Hand()

    deck = blackjack.Deck()
    deck.shuffle()

    dealer.add(deck.draw())
    player.add(deck.draw())
    dealer.add(deck.draw())
    player.add(deck.draw())

    print(f"Dealer upcard: {dealer.cards[1].show()}")
    print("Player's cards:", [i.show() for i in player.cards])
    print(f"Player total: {player.total}")

    # First check: Blackjacks?
    player_blackjack = checks.check_blackjack(player)
    dealer_blackjack = checks.check_blackjack(dealer)

    if player_blackjack is True and dealer_blackjack is True:
        print(f"Dealer's hidden card: {dealer.cards[0].show()}")
        print("Both blackjack: Tie")

        return (0, 0, 0, 0)

    elif player_blackjack is True:
        print("Player blackjack: Win")

        return (1, 1, 1.5, 0)

    elif dealer_blackjack is True:
        print(f"Dealer's hidden card: {dealer.cards[0].show()}")
        print("Dealer blackjack: Loss")

        return (1, 0, 0, 1)

    print("Player's turn")
    player_hand = strategies.player_hand(player, dealer, deck)

    # Check for all busts
    if all(i[0] > 21 for i in player_hand):
        print("Busted: Loss")
        wins = 0
        hands = 1
        payout = 0
        loss = len(player_hand)

        return (hands, wins, payout, loss)

    # Check for all blackjacks
    elif all(i[1] == 1.5 for i in player_hand):
        print("Blackjacks: Win")
        hands = 1
        wins = 1
        payout = 1.5 * len(player_hand)
        loss = 0

        return (hands, wins, payout, loss)

    print("Dealer's turn")
    dealer_hand = strategies.dealer_hand(dealer, deck)

    if dealer_hand[0] > 21:
        print("Dealer busted: Win")
        hands = 1
        wins = 1
        payout = len(player_hand)
        loss = 0

        return (hands, wins, payout, loss)

    hands = 0
    wins = 0
    payout = 0
    loss = 0
    dealer_total = dealer_hand[0]
    print(f"Dealer total: {dealer_total}")
    for i in player_hand:
        player_total = i[0]
        multiplier = i[1]
        print(f"Player total: {player_total}")
        if player_total == dealer_total:
            print("Tie")

        elif i[0] < dealer_hand[0]:
            print("Loss")
            hands += 1
            loss += multiplier

        else:
            print("Win")
            hands += 1
            wins += 1
            payout += multiplier

    sys.stdout = sys.__stdout__

    return (hands, wins, payout, loss)
