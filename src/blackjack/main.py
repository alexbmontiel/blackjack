"""
This module contains the command line argument parsing tools.
"""
import argparse

import src.blackjack.loop as loop


parser = argparse.ArgumentParser(
    description="Play hands of blackjack using optimal strategy and track results."
)

parser.add_argument(
    "-n",
    "--n_hands",
    type=int,
    default=1000,
    help="Number of hands (default: 1000)"
)
parser.add_argument(
    "-p",
    "--parallel",
    action="store_true",
    help="Parallelize using all available cores (default: sequential)"
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Print game details (default: silence prints)"
)

if __name__ == "__main__":
    args = parser.parse_args()
    loop.main(
        n_hands=args.n_hands,
        parallel=args.parallel,
        verbose=args.verbose
    )
