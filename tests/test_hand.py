import unittest
from poker.hand import Hand
from poker.card import Card

class HandTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='4', suit='Clubs')
        ]

        hand = Hand(cards = cards)
        self.assertEqual(
            hand.cards,
            cards
                         )
    
    def test_figures_out_high_caris_best_rank(self):
        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='4', suit='Clubs')
        ]

        hand = Hand(cards = cards)
        self.assertEqual(
            hand.best_rank(),
            'High Card'
        )