import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Hearts", 2)
        self.card2 = Card("Diamonds", 4)
        self.card3 = Card("Spades", 1)
        self.cards = [self.card1, self.card2, self.card3]
        self.game = CardGame

    def test_check_for_ace(self):
        self.assertEqual(True, self.card3.value)

    def test_highest_card(self):
        output = self.game.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, output)

    def test_cards_total(self):
        output = self.game.cards_total(self, self.cards)
        self.assertEqual("You have a total of 7", output)





    