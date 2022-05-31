import blackjack


def replace_ace(hand: blackjack.Hand) -> blackjack.Hand:
    """Replace an ace in a hand with a 1"""
    cards = hand.cards
    first_ace = next(card for card in cards if card.value == "Ace")
    first_ace_suit = first_ace.suit
    cards.remove(first_ace)
    new_card = blackjack.Card("1", first_ace_suit)
    cards.append(new_card)
    new_hand = blackjack.Hand(*cards)

    return new_hand

