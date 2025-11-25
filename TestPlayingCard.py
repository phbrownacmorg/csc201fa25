import unittest
# import the code you want to test here
from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testLegalConstruction(self) -> None:
        for suit in PlayingCard.SUITS:
            for rank in PlayingCard.RANKS:
                with self.subTest(suit=suit, rank=rank):
                    card = PlayingCard(suit, rank)
                    self.assertEqual(card.suit(), suit)
                    self.assertEqual(card.rank(), rank)

    def testIllegalSuitConstruction(self) -> None:
        with self.assertRaises(ValueError) as cm:
            PlayingCard('raspberries', '3')
        self.assertEqual(cm.exception.args[0], f'suit "raspberries" is not one of {PlayingCard.SUITS}')

    def testIllegalRankConstruction(self) -> None:
        with self.assertRaises(ValueError) as cm:
            PlayingCard('hearts', 'alligator')
        self.assertEqual(cm.exception.args[0], f'rank "alligator" is not one of {PlayingCard.RANKS}')

    def testStr(self) -> None:
        for suit in PlayingCard.SUITS:
            for rank in PlayingCard.RANKS:
                with self.subTest(suit=suit, rank=rank):
                    self.assertEqual(str(PlayingCard(suit, rank)), f'{rank} of {suit}')

    def testEqCards(self) -> None:
        for suit1 in PlayingCard.SUITS:
            for rank1 in PlayingCard.RANKS:
                card1 = PlayingCard(suit1, rank1)
                for suit2 in PlayingCard.SUITS:
                    for rank2 in PlayingCard.RANKS:
                        card2 = PlayingCard(suit2, rank2)
                        with self.subTest(suit1=suit1,rank1=rank1,suit2=suit2,rank2=rank2):
                            if suit1 == suit2 and rank1 == rank2:
                                self.assertTrue(card1 == card2)
                            else:
                                self.assertFalse(card1 == card2)

    def testEqNonCard(self) -> None:
        self.assertFalse(PlayingCard('diamonds', 'jack') == 'jack of diamonds')

    def testLt(self) -> None:
        for suit1 in PlayingCard.SUITS:
            for rank1 in PlayingCard.RANKS:
                card1 = PlayingCard(suit1, rank1)
                suit_idx1 = PlayingCard.SUITS.index(card1.suit())
                rank_idx1 = PlayingCard.RANKS.index(card1.rank())
                for suit2 in PlayingCard.SUITS:
                    for rank2 in PlayingCard.RANKS:
                        card2 = PlayingCard(suit2, rank2)
                        suit_idx2 = PlayingCard.SUITS.index(card2.suit())
                        rank_idx2 = PlayingCard.RANKS.index(card2.rank())
                        with self.subTest(suit1=suit1,rank1=rank1,suit2=suit2,rank2=rank2):
                            if suit_idx1 < suit_idx2:
                                self.assertTrue(card1 < card2)
                            elif card1.suit() == card2.suit() and rank_idx1 < rank_idx2:
                                self.assertTrue(card1 < card2)
                            else:
                                self.assertFalse(card1 < card2)

if __name__ == '__main__':
    unittest.main()

