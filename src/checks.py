"""This module contains functions to check the basic strategy tables for
how to proceed, based on player's hand and dealer's up card.

Note: We assume we can only see the dealer's second card, hence the line

    `dealer_card = dealer.cards[1].show()[0]`

in most functions in this module. This grabs the first index (card number)
of the dealer's second card."""

import src.tables as tables
import src.blackjack as blackjack


def check_blackjack(player: blackjack.Hand) -> bool:
    """Checks if player's hand is a blackjack"""
    player_cards = player.card_types

    if player_cards in tables.blackjack_hands:
        return True
    else:
        return False


def check_split(player: blackjack.Hand, dealer: blackjack.Hand) -> bool:
    """Checks if player should split hand"""
    player_card = str(player.card_types.copy().pop())
    dealer_card = dealer.cards[1].show()[0]

    split = tables.split_hands.get(player_card, {}).get(dealer_card, False)

    return split


def soft_double_down(player: blackjack.Hand, dealer: blackjack.Hand) -> bool:
    """Checks if player should double down if they have an Ace"""
    player_total_minus_ace = str(player.total - 11)
    dealer_card = dealer.cards[1].show()[0]

    double_down = tables.soft_double_down.get(player_total_minus_ace, {}).get(dealer_card, False)

    return double_down


def hard_double_down(player: blackjack.Hand, dealer: blackjack.Hand) -> bool:
    """Checks if player should double down if they have no Ace"""
    player_total = str(player.total)
    dealer_card = dealer.cards[1].show()[0]

    double_down = tables.hard_double_down.get(player_total, {}).get(dealer_card, False)

    return double_down


def check_soft_hit(player: blackjack.Hand, dealer: blackjack.Hand):
    """Checks if player should hit, if they have an Ace. If False, stand."""
    player_total_minus_ace = str(player.total - 11)
    dealer_card = dealer.cards[1].show()[0]

    hit = tables.soft_hit.get(player_total_minus_ace, {}).get(dealer_card, False)

    return hit


def check_hard_hit(player: blackjack.Hand, dealer: blackjack.Hand) -> bool:
    """Checks if player should hit, if they have no Ace. If False, stand."""
    player_total = str(player.total)
    dealer_card = dealer.cards[1].show()[0]

    hit = tables.hard_hit.get(player_total, {}).get(dealer_card, False)

    return hit

