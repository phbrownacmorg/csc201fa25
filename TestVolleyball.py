import unittest
# import the code you want to test here
from sim_volleyball import *
import random

class TestVolleyball(unittest.TestCase):

    # setUp, if it exists, will be run before every test
    def setUp(self) -> None:
        random.seed(20251113)
        # First random value is 0.6691087344005507

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # Generic case, both less than win_pts
    def testGameOverRally10_15(self) -> None: 
        self.assertFalse(gameOver(10,15,25))

    # Boundary case, both less than win_pts
    def testGameOverRally24_24(self) -> None: 
        self.assertFalse(gameOver(24,24,25))

    # One score == win_pts, generic difference between scores
    def testGameOverRally25_20(self) -> None: 
        self.assertTrue(gameOver(25,20,25))

    # One score == win_pts, minimum difference to win (boundary)
    def testGameOverRally23_25(self) -> None: 
        self.assertTrue(gameOver(23,25,25))

    # One score == win_pts, maximum difference *not* to win (boundary)
    def testGameOverRally25_24(self) -> None: 
        self.assertFalse(gameOver(25,24,25))

    # One score > win_pts, minimum difference to win (boundary)
    def testGameOverRally26_24(self) -> None:
        self.assertTrue(gameOver(26,24,25))

    # Both scores > win_pts (generic), maximum difference not to win (boundary)
    def testGameOverRally28_29(self) -> None:
        self.assertFalse(gameOver(28,29,25))

    # Both scores > win_pts (generic), minimum difference to win (boundary)
    def testGameOverRally28_30(self) -> None:
        self.assertTrue(gameOver(28,30,25))

    # Repeat the same cases for sideout scoring (win_pts == 15)
    def testGameOverSideOut10_13(self) -> None:
        self.assertFalse(gameOver(10,13,15))

    def testGameOverSideOut14_14(self) -> None:
        self.assertFalse(gameOver(14,14,15))

    def testGameOverSideOut15_10(self) -> None:
        self.assertTrue(gameOver(15,10,15))

    def testGameOverSideOut13_15(self) -> None:
        self.assertTrue(gameOver(13,15,15))

    def testGameOverSideOut15_14(self) -> None:
        self.assertFalse(gameOver(15,14,15))

    def testGameOverSideOut16_14(self) -> None:
        self.assertTrue(gameOver(16,14,15))

    def testGameOverSideOut28_29(self) -> None:
        self.assertFalse(gameOver(28,29,15))

    def testGameOverSideOut28_30(self) -> None:
        self.assertTrue(gameOver(28,30,15))

    # Generic probabilities (well clear of random value), pA < pB, A serves
    def testSimRallyp6p7A(self) -> None:
        self.assertFalse(simulateRally(.6, .7, True))

    # Generic probabilities (well clear of random value), pA < pB, B serves
    def testSimRallyp6p7B(self) -> None:
        self.assertFalse(simulateRally(.6, .7, False))

    # Generic probabilities (well clear of random value), pA > pB, A serves
    def testSimRallyp7p6A(self) -> None:
        self.assertTrue(simulateRally(.7, .6, True))

    # Generic probabilities (well clear of random value), pA > pB, B serves
    def testSimRallyp7p6B(self) -> None:
        self.assertTrue(simulateRally(.7, .6, False))

    # Boundary probabilities (pA == pB > random value), A serves
    def testSimRallyp67p67A(self) -> None:
        self.assertTrue(simulateRally(.6691087344005508, .6691087344005508, True))

    # Boundary probabilities (pA == pB > random value), B serves
    def testSimRallyp67p67B(self) -> None:
        self.assertFalse(simulateRally(.6691087344005508, .6691087344005508, False))

    # Boundary probabilities (pA == pB < random value), A serves
    def testSimRallyp66p66A(self) -> None:
        self.assertFalse(simulateRally(.6691087344005506, .6691087344005506, True))

    # Boundary probabilities (pA == pB < random value), B serves
    def testSimRallyp66p66B(self) -> None:
        self.assertTrue(simulateRally(.6691087344005506, .6691087344005506, False))

    # Simulate 1 game, sideout scoring
    def testSim1Gamep67p67Sideout(self) -> None:
        self.assertTrue(simulate1Game(.6691087344005508, .6691087344005508, True))

    # Simulate 1 game, rally scoring
    def testSim1Gamep67p67Rally(self) -> None:
        self.assertFalse(simulate1Game(.6691087344005508, .6691087344005508, False))

    # Simulate 15 games, rally scoring
    def testSimNGamesp67p67Rally(self) -> None:
        # 11/15 is pretty lopsided for two evenly-matched teams, but 15 games is not a lot
        self.assertAlmostEqual(simulateNGames(15, .6691087344005508, .6691087344005508, False), 11/15)

    # Simulate 15 games, sideout scoring
    def testSimNGamesp67p67SideOut(self) -> None:
        # 11/15 is pretty lopsided for two evenly-matched teams, but 15 games is not a lot
        self.assertAlmostEqual(simulateNGames(15, .6691087344005508, .6691087344005508, True), 8/15)

if __name__ == '__main__':
    unittest.main()

