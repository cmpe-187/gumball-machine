import unittest
import gumball_machine as gumball_machine_class


class NoCurrencyTestCases(unittest.TestCase):
    def setUp(self):
        self.gumball_machine = gumball_machine_class.GumballMachine()

    def test_dispense_red(self):
        """Tests dispensing a red gumball with no currency in the machine"""
        # input: dispense_red()
        expected_output = "You need at least 5 cents to dispense a red gumball"

        actual_output = self.gumball_machine.dispense_red()
        self.assertEqual(expected_output, actual_output)

    def test_dispense_yellow(self):
        """Tests dispensing a yellow gumball with no currency in the machine"""
        # input: dispense_yellow()
        expected_output = "You need at least 10 cents to dispense a yellow gumball"

        actual_output = self.gumball_machine.dispense_yellow()
        self.assertEqual(expected_output, actual_output)

    def test_return_my_change(self):
        """Tests returning change with no currency in the machine"""
        # input: return_my_change()
        expected_output = "There is no change to return"

        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)


class ReturnValidCurrencyTestCases(unittest.TestCase):
    def setUp(self):
        self.gumball_machine = gumball_machine_class.GumballMachine()

    def test_return_nickel(self):
        """Tests inserting a nickel, then returning change"""
        # input: insert("nickel"), return_my_change()
        expected_output = "Returning your change of 5 cents"

        self.gumball_machine.insert("nickel")
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

    def test_return_dime(self):
        """Tests inserting a dime, then returning change"""
        # input: insert("dime"), return_my_change()
        expected_output = "Returning your change of 10 cents"

        self.gumball_machine.insert("dime")
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

    def test_return_quarter(self):
        """Tests inserting a quarter, then returning change"""
        # input: insert("quarter"), return_my_change()
        expected_output = "Returning your change of 25 cents"

        self.gumball_machine.insert("quarter")
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)


class ExactCurrencyTestCases(unittest.TestCase):
    def setUp(self):
        self.gumball_machine = gumball_machine_class.GumballMachine()

    def test_insert_nickel_dispense_red(self):
        """Tests dispensing a red gumball with a nickel (5 cents) in the machine"""
        # input: insert("nickel"), dispense_red()
        expected_output = "Enjoy your red gumball"

        self.gumball_machine.insert("nickel")
        actual_output = self.gumball_machine.dispense_red()
        self.assertEqual(expected_output, actual_output)

    def test_insert_dime_dispense_yellow(self):
        """Tests dispensing a yellow gumball with a dime (10 cents) in the machine"""
        # input: insert("dime"), dispense_yellow()
        expected_output = "Enjoy your yellow gumball"

        self.gumball_machine.insert("dime")
        actual_output = self.gumball_machine.dispense_yellow()
        self.assertEqual(expected_output, actual_output)

    def test_insert_nickels_dispense_yellow(self):
        """Tests dispensing a yellow gumball with two nickels (10 cents) in the machine"""
        # input: insert("nickel"), insert("nickel"), dispense_yellow()
        expected_output = "Enjoy your yellow gumball"

        self.gumball_machine.insert("nickel")
        self.gumball_machine.insert("nickel")
        actual_output = self.gumball_machine.dispense_yellow()
        self.assertEqual(expected_output, actual_output)


class InvalidCurrencyTestCases(unittest.TestCase):
    def setUp(self):
        self.gumball_machine = gumball_machine_class.GumballMachine()

    def test_return_dollar(self):
        """Tests inserting a dollar, then returning change"""
        # input: insert("dollar"), return_my_change()
        expected_output = "Returning your invalid currency of dollar"

        self.gumball_machine.insert("dollar")
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

    def test_return_dollars(self):
        """Tests inserting multiple dollars, then returning change"""
        # input: insert("dollar"), insert("dollar"), return_my_change()
        expected_output = "Returning your invalid currency of dollar, dollar"

        self.gumball_machine.insert("dollar")
        self.gumball_machine.insert("dollar")
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

    def test_insert_dollar_dispense_red(self):
        """Tests inserting a dollar, then attempting to dispense a red gumball"""
        # input: insert("dollar"), dispense_red()
        expected_output = "Returning your invalid currency of dollar"

        self.gumball_machine.insert("dollar")
        actual_output = self.gumball_machine.dispense_red()
        self.assertEqual(expected_output, actual_output)

    def test_insert_dollar_dispense_yellow(self):
        """Tests inserting a dollar, then attempting to dispense a yellow gumball"""
        # input: insert("dollar"), yellow()
        expected_output = "Returning your invalid currency of dollar"

        self.gumball_machine.insert("dollar")
        actual_output = self.gumball_machine.dispense_yellow()
        self.assertEqual(expected_output, actual_output)


class MultipleGumballsExactCurrencyTestCases(unittest.TestCase):
    def setUp(self):
        self.gumball_machine = gumball_machine_class.GumballMachine()

    def test_insert_nickels_dispense_reds(self):
        """Tests inserting 2 nickels, and dispensing 2 red gumballs"""
        # input: insert("nickel"), insert("nickel"), dispense_red(), dispense_red(), return_my_change()
        expected_output = "There is no change to return"

        self.gumball_machine.insert("nickel")
        self.gumball_machine.insert("nickel")
        self.gumball_machine.dispense_red()
        self.gumball_machine.dispense_red()
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

    def test_insert_dime_dispense_reds(self):
        """Tests inserting a dime, and dispensing 2 red gumballs"""
        # input: insert("dime"), dispense_red(), dispense_red(), return_my_change()
        expected_output = "There is no change to return"

        self.gumball_machine.insert("dime")
        self.gumball_machine.dispense_red()
        self.gumball_machine.dispense_red()
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

    def test_insert_nickels_dispense_yellows(self):
        """Tests inserting 4 nickels, and dispensing 2 yellow gumballs"""
        # input: insert("nickel"), insert("nickel"), insert("nickel"), insert("nickel"), dispense_yellow(), dispense_yellow(), return_my_change()
        expected_output = "There is no change to return"

        self.gumball_machine.insert("nickel")
        self.gumball_machine.insert("nickel")
        self.gumball_machine.insert("nickel")
        self.gumball_machine.insert("nickel")
        self.gumball_machine.dispense_yellow()
        self.gumball_machine.dispense_yellow()
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

    def test_insert_dimes_dispense_yellows(self):
        """Tests inserting 2 dimes, and dispensing 2 yellow gumballs"""
        # input: insert("dime"), insert("dime"), dispense_yellow(), dispense_yellow(), return_my_change()
        expected_output = "There is no change to return"

        self.gumball_machine.insert("dime")
        self.gumball_machine.insert("dime")
        self.gumball_machine.dispense_yellow()
        self.gumball_machine.dispense_yellow()
        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)

if __name__ == '__main__':
    unittest.main()
