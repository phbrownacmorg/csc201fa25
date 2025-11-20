import unittest
# import the code you want to test here
from eligibility import eligibleHR, parseInput

class TestEligibility(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # T, T, boundaries
    def testeligibleHR_25_7(self) -> None:
        self.assertTrue(eligibleHR(25, 7))

    # T, F, boundaries
    def testeligibleHR_25_6(self) -> None:
        self.assertFalse(eligibleHR(25, 6))

    # F, T, boundaries
    def testeligibleHR_24_7(self) -> None:
        self.assertFalse(eligibleHR(24, 7))

    # F, F, boundaries
    def testeligibleHR_24_6(self) -> None:
        self.assertFalse(eligibleHR(24, 6))

    # T, T, generic
    def testeligibleHR_30_15(self) -> None:
        self.assertTrue(eligibleHR(30, 15))

    # T, F, generic
    def testeligibleHR_27_3(self) -> None:
        self.assertFalse(eligibleHR(27, 3))

    # F, T, generic
    def testeligibleHR_15_15(self) -> None:
        self.assertFalse(eligibleHR(15, 15))

    # F, F, generic
    def testeligibleHR_4_4(self) -> None:
        self.assertFalse(eligibleHR(4, 4))

    def testParseInput_OK(self) -> None:
        self.assertEqual(parseInput('35', '35'), (35, 35))

    def testParseInput_negAge(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('-1', '15')
        self.assertEqual(cm.exception.args[0], 'Age cannot be negative.')

    def testParseInput_negCit(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('45', '-15')
        self.assertEqual(cm.exception.args[0], 'Years of citizenship cannot be negative.')

    def testParseInput_CitOverAge(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('25', '35')
        self.assertEqual(cm.exception.args[0], 'Years of citizenship cannot be greater than age.')

    def testParseInput_AgeStr(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('old', '35')
        self.assertEqual(cm.exception.args[0], 'Age must be a non-negative integer.')

    def testParseInput_CitStr(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('35', 'all my life')
        self.assertEqual(cm.exception.args[0], 'Years of citizenship must be a non-negative integer.')

    def testParseInput_AgeFloat(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('36.5', '35')
        self.assertEqual(cm.exception.args[0], 'Age must be a non-negative integer.')

    def testParseInput_CitFloat(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('35', '3.5')
        self.assertEqual(cm.exception.args[0], 'Years of citizenship must be a non-negative integer.')

    def testParseInput_CitUnits(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseInput('35', '5 years')
        self.assertEqual(cm.exception.args[0], 'Years of citizenship must be a non-negative integer.')


if __name__ == '__main__':
    unittest.main()

