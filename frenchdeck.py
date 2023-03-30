from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str


"""
Source : https://github.com/fluentpython/example-code-2e/blob/master/01-data-model/frenchdeck.py
"""


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


d = FrenchDeck()
print(f"Size the this deck is - %d" % len(d))
for c in d:
    print(c)
Card
c = Card("7", "Diamonds")
print(f"Does  this deck has %s, - %s" % (c, c in d))
from random import choice

print(f"Random card chosen - %s" % choice(d))
