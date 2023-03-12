import random
import itertools


class SetGame:
    """
        Represents a game of Set.

        Attributes:
            shapes (list): A list of the possible shapes for a Set card.
            colors (list): A list of the possible colors for a Set card.
            numbers (list): A list of the possible numbers for a Set card.
            shadings (list): A list of the possible shadings for a Set card.
            deck (list): A list containing all possible combinations of shapes, colors, numbers, and shadings
                to form the Set game deck.

        Methods:
            __init__(): Initializes a SetGame object and creates a deck of cards.
            draw(): Draws 12 cards randomly from the deck.
            @staticmethod is_set(): Determines whether a given combination of three cards form a Set. @staticmethod
            play(): Returns all possible Sets that can be formed from 12 cards drawn.
            check_set_exist(): Returns True if at least one Set can be formed from the current selection of cards,
                False otherwise.
        """
    shapes = ['oval', 'squiggles', 'dimond']
    colors = ['red', 'purple', 'green']
    numbers = [1, 2, 3]
    shadings = ['solid', 'striped', 'outlined']

    def __init__(self):
        self.deck = list(itertools.product(SetGame.shapes, SetGame.colors, SetGame.numbers, SetGame.shadings))

    def draw(self):
        """""Draw 12 cards randomly from the deck."""
        return random.sample(self.deck, 12)

    @staticmethod
    def is_set(card1, card2, card3):
        """Determine whether a given combination of three cards form a Set"""
        for index in range(4):
            if len({card1[index], card2[index], card3[index]}) == 2:
                return False
        return True

    def play(self):
        """Return all possible Sets that can be formed from 12 cards drawn"""
        selection = self.draw()
        return [list(combo) for combo in itertools.combinations(selection, 3) if SetGame.is_set(*combo)]

    def check_set_exist(self):
        """Return True if at least one Set can be formed from the current selection of cards"""
        return len(self.play()) != 0


# This program tests analytics for the SetGame class, by drawing 12 cards 100000 times
# and checking the percentage of times there is no set among the drawn cards.
def main():
    game = SetGame()
    count = sum(not game.check_set_exist() for _ in range(10000))
    print("percentage of draws with no sets att all: ", count / 10000)


if __name__ == "__main__":
    main()
