import unittest
from poker.card import Card



class CardTest(unittest.TestCase): 
    def test_card_has_rank(self):
        Card(rank = "Queen", suit = "Hearts")