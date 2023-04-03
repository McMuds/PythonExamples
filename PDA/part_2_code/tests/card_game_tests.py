import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.acecard = Card("Diamonds", 1)
        self.kingcard = Card("Hearts", 13)
        self.tencard = Card("Spades", 10)
        self.twocard = Card("Clubs",2)
        self.cardgame = CardGame()

    def test_check_for_ace(self):
        # cardgame = CardGame()
        actual = self.cardgame.check_for_ace(self.acecard)
        self.assertEqual (True, actual)

    def test_check_fo_ace__fail(self):
        actual = self.cardgame.check_for_ace(self.kingcard)
        self.assertEqual(False, actual)

    def test_highest_card__card1(self):
        actual = self.cardgame.highest_card(self.tencard, self.twocard)
        self.assertEqual(self.tencard,actual)

    def test_highest_card__card2(self):
        actual = self.cardgame.highest_card(self.twocard, self.kingcard)
        self.assertEqual(self.kingcard, actual)

    def test_cards_total(self):
        cards = [self.acecard, self.kingcard, self.tencard]
        actual = self.cardgame.cards_total(cards)
        self.assertEqual("You have a total of 24", actual)