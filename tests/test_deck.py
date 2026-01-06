import unittest
from poker.deck import Deck

class DeckCard(unittest.TestCase):
    def test_has_no_card_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_add_cards_to_its_collection(self):
        deck = Deck()
        deck.add_cards()