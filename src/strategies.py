"""
This module contains the code to play both the player's hand and the
dealer's hand. The player's hand is played optimally according to
the dealer's face up card. The dealer's hand follows traditional
casino rules.
"""

import blackjack
import checks
import utils


def player_hand(player, dealer, deck):
    """Add cards to hand based on optimal strategy
    and returns total and multiplier for each hand.

    Needs to return a list in case of splits.

    Args:
      player (Hand): Player's current hand
      dealer (Hand): Dealer's current hand
      deck (Deck): Current deck

    Returns:
      hands (list): List of tuples (player.total, multiplier)

    Multipliers:
      Blackjack: 1.5
      Double down: 2
      Normal hit: 1
    """
    while len(player.cards) < 2:
        player.add(deck.draw())

    # Second check: Split?
    if len(player.card_types) == 1:
        #check split table
        split = checks.check_split(player, dealer)

        if split is True:
            print("Action: Split")
            card_1 = player.cards[0]
            card_2 = player.cards[1]

            hand_1 = player_hand(blackjack.Hand(card_1), dealer, deck)
            hand_2 = player_hand(blackjack.Hand(card_2), dealer, deck)
            hands = hand_1 + hand_2

            return hands

    # Third check: Double down?
    if len(player.cards) == 2:
        if "Ace" in player.card_types:
            # check soft double down table
            double_down = checks.soft_double_down(player, dealer)
        else:
            # check double down table
            double_down = checks.hard_double_down(player, dealer)

        if double_down is True:
            print("Action: Double down")
            player.add(deck.draw())
            print("Player's cards:", [i.show() for i in player.cards])
            print(f"Player total: {player.total}")

            if player.total > 21 and "Ace" in player.card_types:
                print("Replace Ace")
                player = utils.replace_ace(player)
                print(f"Player total: {player.total}")

            return [(player.total, 2)]

    hit = None
    # Fourth check: Hit?
    while hit is not False:
        if player.total > 21:
            if "Ace" in player.card_types:
                #replace with 1
                player = utils.replace_ace(player)
                print("Replace Ace")
                print(f"Player total: {player.total}")
            else:
                print("Bust!")

                return [(player.total, 1)]

        if "Ace" in player.card_types:
            # check soft hit table
            hit = checks.check_soft_hit(player, dealer)
        else:
            hit = checks.check_hard_hit(player, dealer)

        if hit is True:
            print("Action: Hit")
            player.add(deck.draw())
            print("Player's cards:", [i.show() for i in player.cards])
            print(f"Player total: {player.total}")
        else:
            print("Action: Stand")
            return [(player.total, 1)]

    return [(player.total, 1)]


def dealer_hand(dealer, deck):
    """Play dealer hand accoring to basic blackjack rules of
    drawing until 17, either hard or soft.

    Args:
      dealer:
      deck:

    Returns:
    """
    while len(dealer.cards) < 2:
        dealer.add(deck.draw())

    print("Dealer's cards:", [i.show() for i in dealer.cards])
    print(f"Dealer total: {dealer.total}")

    while dealer.total < 17:
        print("Action: Hit")
        dealer.add(deck.draw())
        print("Dealer cards:", [i.show() for i in dealer.cards])
        print(f"Dealer total: {dealer.total}")

        if dealer.total > 21:
            if "Ace" in dealer.card_types:
                print("Replace Ace")
                dealer = utils.replace_ace(dealer)
                print(f"Dealer total: {dealer.total}")
            else:
                print("Bust!")
                return (dealer.total, 1)

    print("Action: Stand")
    return (dealer.total, 1)


if __name__ == "__main__":
    test = None
    while test is None:
        player = blackjack.Hand()
        dealer = blackjack.Hand()
        deck = blackjack.Deck()
        deck.shuffle()
        dealer.add(deck.draw())
        player.add(deck.draw())
        dealer.add(deck.draw())
        player.add(deck.draw())
#        test = player_hand(player, dealer, deck)
        test = dealer_hand(dealer, deck)
        print(test)

