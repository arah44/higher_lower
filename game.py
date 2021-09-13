from cards import Deck, Card, NUMBERS


class Player:
    def __init__(self, name, player_type="bot") -> None:
        self.name = name
        self.win_count = 0
        self.loss_count = 0
        self.player_type = player_type
        self.card_count = {num: 4 for num in NUMBERS}

    def __str__(self) -> str:
        return f"{self.name}: {self.win_count} wins | {self.loss_count} losses | {self.win_count / (self.win_count + self.loss_count):.2f}%"

    def update_card_count(self, card: Card):
        """Updates the card count by decrementing the given card number"""
        self.card_count[card.number] -= 1

    def get_proba(self, card: Card, deck_length: int):
        """Given the deck, calculate the probability of a higher card"""
        
        # Update card count before calculating probability
        self.update_card_count(card)

        # Caculate the cumulative probability of getting a value higher than card.
        proba = 0
        for i in list(self.card_count.keys())[card.number:]:
            proba += self.card_count[i] / deck_length

        return 'higher' if proba > 0.5 else 'lower'

    def take_turn(self, card: Card = None, deck_length: int = None) -> str:
        """Given a card, guess if the next card is going to be higher or lower"""
        if self.player_type == "human":
            return input("Guess: ")

        # Otherwise calculate using probability
        return self.get_proba(card, deck_length)


class Game:
    def __init__(self) -> None:
        self.deck = Deck()


class HigherLower(Game):
    """A card is drawn, players take turns to guess if the next card will be higher or lower than the current card."""

    def __init__(self) -> None:
        super().__init__()
        self.player_1 = Player("Player 1", player_type="human")
        self.player_2 = Player("Player 2")

        # Draw the first card
        self.pre_card = self.deck.draw_card()
        self.post_card = None

        # Print game intro
        print(
            """
        Welcome to higher or lower.

        Guess if the next card will be higher or lower than the current card.

        Game plays until no more cards are available or input from player is 'q'
        """
        )

    def finished(self) -> bool:
        if self.deck.num_cards() == 0:
            return True
        return False

    def print_winner(self):
        """Calculate winner based on number of wins"""

        print("\n" + "*" * 15)
        print(self.player_1)
        print(self.player_2)
        print("*" * 15)

        if self.player_1.win_count > self.player_2.win_count:
            print("\nPlayer 1 wins!!!")
            return self.player_1
        elif self.player_1.win_count < self.player_2.win_count:
            print("\nPlayer 2 wins!!!")
        else:
            print("\nDraw!")

    def play(self):
        """Ask players for guess and update result"""

        print(f"\nCard: {self.pre_card}")
        guess_1 = self.player_1.take_turn()
        guess_2 = self.player_2.take_turn(self.pre_card, self.deck.num_cards())

        # End game with q
        if guess_1 == "q":
            print("Game ended")
            return self.print_winner()

        # Check valid input
        elif guess_1 not in ["higher", "lower"]:
            print("Guess must be 'higher' or 'lower'")
            guess_1 = self.player_1.take_turn()

        # Draw a new card
        self.post_card = self.deck.draw_card()

        print(f"Player 1 guess: {guess_1}")
        print(f"Player 2 guess: {guess_2}")

        if guess_1 == "higher":
            self.player_1.win_count += 1 if self.pre_card <= self.post_card else 0
            self.player_1.loss_count += 1 if self.pre_card >= self.post_card else 0
        else:
            self.player_1.win_count += 1 if self.pre_card >= self.post_card else 0
            self.player_1.loss_count += 1 if self.pre_card <= self.post_card else 0

        if guess_2 == "higher":
            self.player_2.win_count += 1 if self.pre_card <= self.post_card else 0
            self.player_2.loss_count += 1 if self.pre_card >= self.post_card else 0
        else:
            self.player_2.win_count += 1 if self.pre_card >= self.post_card else 0
            self.player_2.loss_count += 1 if self.pre_card <= self.post_card else 0

        # Reset hand
        self.pre_card = self.post_card
        self.post_card = None

        # Continue until finished
        if not self.finished():
            return self.play()

        # Return and print winner
        return self.print_winner()


game = HigherLower()
game.play()
