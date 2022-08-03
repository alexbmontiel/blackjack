blackjack_hands = [
    set(["Ace", "10"]),
    set(["Ace", "Jack"]),
    set(["Ace", "Queen"]),
    set(["Ace", "King"])
]


split_hands = {
    # Player's card
    "2": {
        # Dealer's upcard
        j: True for j in [str(k) for k in range(2, 8)]
    },
    "3": {
        j: True for j in [str(k) for k in range(2, 8)]
    },
    "4": {
        j: True for j in ["5", "6"]
    },
    "6": {
        j: True for j in [str(k) for k in range(2, 7)]
    },
    "7": {
        j: True for j in [str(k) for k in range(2, 8)]
    },
    "8": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "9": {
        j: True for j in [str(k) for k in range(2, 7)] + ["8", "9"]
    },
    "Ace": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    }
}


soft_double_down = {
    "2": {
        j: True for j in ["5", "6"]
    },
    "3": {
        j: True for j in ["5", "6"]
    },
    "4": {
        j: True for j in ["4", "5", "6"]
    },
    "5": {
        j: True for j in ["4", "5", "6"]
    },
    "6": {
        j: True for j in ["3", "4", "5", "6"]
    },
    "7": {
        j: True for j in ["2", "3", "4", "5", "6"]
    },
    "8": {
        "6": True
    }
}


hard_double_down = {
    "9": {
        j: True for j in [str(k) for k in range(3, 7)]
    },
    "10": {
        j: True for j in [str(k) for k in range(2, 10)]
    },
    "11": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    }
}


soft_hit = {
    "2": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "3": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "4": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "5": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "6": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "7": {
        j: True for j in ["9", "10"] + ["Jack", "Queen", "King", "Ace"]
    }
}


hard_hit = {
    "2": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "3": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "4": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "5": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "6": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "7": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "8": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "9": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "10": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "11": {
        j: True for j in [str(k) for k in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "12": {
        j: True for j in ["2", "3"] + [str(k) for k in range(7, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "13": {
        j: True for j in [str(k) for k in range(7, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "14": {
        j: True for j in [str(k) for k in range(7, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "15": {
        j: True for j in [str(k) for k in range(7, 11)] + ["Jack", "Queen", "King", "Ace"]
    },
    "16": {
        j: True for j in [str(k) for k in range(7, 11)] + ["Jack", "Queen", "King", "Ace"]
    }
}

