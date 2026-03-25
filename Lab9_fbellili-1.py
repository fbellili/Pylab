"""
Program Name: Match Coins Game
Author: Farouk Bellili
Purpose: This program runs a coin matching game between two players.
         Each player tosses a coin and coins are won or lost depending
         on whether the results match.
Starter Code: None
Date: March 24, 2026
"""

from player import Player


def main():

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("\n--- Coin Match Game ---")

    while True:

        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.\n")

        choice = input("Do you want to toss the coins? (y/n): ")

        if choice.lower() != 'y':
            break

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin.\n")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match! Player 2 wins a coin.\n")

        # Challenge: game over if someone reaches 0
        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print("A player has run out of coins. Game over!")
            break

    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins the game!")
    else:
        print("It's a draw!")


main()
