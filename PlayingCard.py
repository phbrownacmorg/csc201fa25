from typing import cast
# Convention: classes are defined in a file that has the same name as the class.

class PlayingCard: # Convention: class names are in CamelCase, starting with a capital letter.
    """Class to represent a standard playing card.  Objects of this class are immutable."""

    # Class variables
    # Convention: anything that functions as a constant is named in ALL CAPS
    SUITS: tuple[str,...] = ('diamonds', 'hearts', 'spades', 'clubs')
    RANKS: tuple[str,...] = tuple(map(str, range(2,11))) + ('jack', 'queen', 'king', 'ace')

    # Constructor
    def __init__(self, suit: str, rank: str) -> None:
        if suit not in self.SUITS:
            raise ValueError(f'suit "{suit}" is not one of {self.SUITS}')
        elif rank not in self.RANKS:
            raise ValueError(f'rank "{rank}" is not one of {self.RANKS}')
        self._suit = suit  # Establish instance variables
        self._rank = rank

    # Accessor/Query/Getter methods

    def suit(self) -> str:
        return self._suit
    
    def rank(self) -> str:
        return self._rank
    
    # Python magic method to return a string representation of a PlayingCard.
    def __str__(self) -> str:
        return self.rank() + ' of ' + self.suit()
    
    # Python magic method, returns True when two objects are equal (== operator)
    def __eq__(self, other: object) -> bool:
        equal: bool = False
        if hasattr(other, 'suit') and hasattr(other, 'rank'):
            equal = (self.rank() == other.rank() and self.suit() == other.suit()) # type: ignore
        return cast(bool, equal)

    # Python magic method.  Returns True when self < other in a standard ordering.
    def __lt__(self, other: 'PlayingCard') -> bool:
        less = False
        if self.SUITS.index(self.suit()) < self.SUITS.index(other.suit()):
            less = True
        elif self.suit() == other.suit() and \
            self.RANKS.index(self.rank()) < self.RANKS.index(other.rank()):
            less = True
        return less

    # I could put in a lot of game-specific query methods.  I prefer, in this
    #     case, to leave those for game-specific subclasses.
    
    # Note no mutator methods.  PlayingCard is immutable, because real playing cards don't change.