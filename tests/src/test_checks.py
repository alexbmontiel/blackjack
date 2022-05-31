import src.checks as checks
import src.blackjack as blackjack


def test_blackjack_true():
    test_hand = blackjack.Hand([
        blackjack.Card("Ace", "Hearts"),
        blackjack.Card("Jack", "Spades")
    ])

    is_blackjack = checks.check_blackjack(test_hand)

    assert is_blackjack is True


def test_blackjack_false():
    test_hand = blackjack.Hand([
        blackjack.Card("Ace", "Hearts"),
        blackjack.Card("3", "Diamonds")
    ])

    is_blackjack = checks.check_blackjack(test_hand)

    assert is_blackjack is False


def test_split_true():
    test_player = blackjack.Hand([
        blackjack.Card("Ace", "Hearts"),
        blackjack.Card("Ace", "Spades")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("2", "Spades"),
        blackjack.Card("5", "Clubs")
    ])

    is_split = checks.check_split(test_player, test_dealer)

    assert is_split is True


def test_split_false():
    test_player = blackjack.Hand([
        blackjack.Card("4", "Diamonds"),
        blackjack.Card("4", "Hearts")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("6", "Spades"),
        blackjack.Card("7", "Clubs")
    ])

    is_split = checks.check_split(test_player, test_dealer)

    assert is_split is False


def test_soft_double_down_true():
    test_player = blackjack.Hand([
        blackjack.Card("3", "Hearts"),
        blackjack.Card("Ace", "Diamonds")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("Ace", "Spades"),
        blackjack.Card("5", "Clubs")
    ])

    is_double_down = checks.soft_double_down(test_player, test_dealer)

    assert is_double_down is True


def test_soft_double_down_false():
    test_player = blackjack.Hand([
        blackjack.Card("3", "Hearts"),
        blackjack.Card("Ace", "Diamonds")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("5", "Clubs"),
        blackjack.Card("Ace", "Spades")
    ])

    is_double_down = checks.soft_double_down(test_player, test_dealer)

    assert is_double_down is False


def test_hard_double_down_true():
    test_player = blackjack.Hand([
        blackjack.Card("5", "Hearts"),
        blackjack.Card("6", "Diamonds")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("Ace", "Spades"),
        blackjack.Card("King", "Clubs")
    ])

    is_double_down = checks.hard_double_down(test_player, test_dealer)

    assert is_double_down is True


def test_hard_double_down_false():
    test_player = blackjack.Hand([
        blackjack.Card("5", "Hearts"),
        blackjack.Card("5", "Diamonds")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("2", "Spades"),
        blackjack.Card("10", "Clubs")
    ])

    is_double_down = checks.hard_double_down(test_player, test_dealer)

    assert is_double_down is False


def test_soft_hit_true():
    test_player = blackjack.Hand([
        blackjack.Card("Ace", "Hearts"),
        blackjack.Card("7", "Diamonds")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("2", "Spades"),
        blackjack.Card("9", "Clubs")
    ])

    is_hit = checks.check_soft_hit(test_player, test_dealer)

    assert is_hit is True



def test_soft_hit_false():
    test_player = blackjack.Hand([
        blackjack.Card("Ace", "Hearts"),
        blackjack.Card("7", "Diamonds")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("9", "Clubs"),
        blackjack.Card("2", "Spades")
    ])

    is_hit = checks.check_soft_hit(test_player, test_dealer)

    assert is_hit is False


def test_hard_hit_true():
    test_player = blackjack.Hand([
        blackjack.Card("10", "Spades"),
        blackjack.Card("5", "Hearts")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("3", "Diamonds"),
        blackjack.Card("7", "Clubs")
    ])

    is_hit = checks.check_hard_hit(test_player, test_dealer)

    assert is_hit is True


def test_hard_hit_false():
    test_player = blackjack.Hand([
        blackjack.Card("10", "Spades"),
        blackjack.Card("5", "Hearts")
    ])
    test_dealer = blackjack.Hand([
        blackjack.Card("7", "Clubs"),
        blackjack.Card("3", "Diamonds")
    ])

    is_hit = checks.check_hard_hit(test_player, test_dealer)

    assert is_hit is False

