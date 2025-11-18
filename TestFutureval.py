import contextlib
import io
import unittest
# import the code you want to test here
from futureval_fns import parseLoan, findTickInterval, calc_balances, printTable


class TestFutureval(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testParseLoan(self) -> None:
        self.assertEqual(parseLoan('1000','3','30'), (1000.0, 3.0, 30))

    def testParseLoanBadP(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('$1,000.00','3','30')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanBadRate(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('1000','3%','30')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanBadPeriods(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('1000','3','30.0')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanNegP(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('-1000','3','30')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanZeroP(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('0','3','30')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanNegRate(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('1000','-0.00000003','30')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanZeroRate(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('1000','0','30')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanNegPeriods(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('1000','3','-1')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testParseLoanZeroPeriods(self) -> None:
        with self.assertRaises(ValueError) as cm:
            parseLoan('1000','3','0')
        self.assertEqual(cm.exception.args[0],
                         "The balance, rate, and periods must all be positive numbers, with no dollar sign, commas, or percent sign.")

    def testFindTickInterval(self) -> None:
        values = list(range(1000, 10001, 1000))
        intervals = [100, 200, 200, 500, 500, 500, 500, 500, 500, 1000]
        for i in range(len(intervals)):
            with self.subTest(val=values[i]):
                self.assertEqual(findTickInterval(values[i]), intervals[i])

    def testCalcBalancesInterest(self) -> None:
        self.assertEqual(calc_balances(1000, 0.01, 3, 0),
                         [1000, 1010, 1020.1, 1030.301])
        self.assertEqual(calc_balances(10000, 0.02, 3, 0),
                         [10000, 10200, 10404, 10612.08])
        p = 1000
        rate = 0.05
        for pds in range(100):
            with self.subTest(pds=pds):
                self.assertAlmostEqual(calc_balances(p, rate, pds, 0)[-1], 
                                       p * (1+rate)**pds)
        
    def testCalcBalancesPayment(self) -> None:
        self.assertAlmostEqual(calc_balances(1000, 0.01, 1, 100)[-1], 910)
        self.assertAlmostEqual(calc_balances(1000, 0.01, 1, 200)[-1], 810)
        self.assertAlmostEqual(calc_balances(1000, 0.01, 2, 100)[-1], 819.10)
        self.assertAlmostEqual(calc_balances(1000, 0.01, 2, 200)[-1], 618.10)

    def testPrintTable(self) -> None:
        balances: list[float] = [1000, 1010, 1020.1, 1030.301]
        out = io.StringIO()
        expected = 'Month\tInterest\tPayment\t\tBalance\n' + ('-' * 70)
        expected += f'\nStart\t\t\t\t\t${balances[0]}\n'
        for i in range(1, len(balances)):
            expected += f'{i+1} \t {round(balances[i] - balances[i-1],2)} '
            expected += f'\t 0 \t {round(balances[i], 2)}\n'
        with contextlib.redirect_stdout(out):
            printTable(balances, 0)
        self.assertEqual(expected, out.getvalue())


if __name__ == '__main__':
    unittest.main()

