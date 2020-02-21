import unittest
import gumball_machine as gumball_machine_class


class NoMoneyTestCases(unittest.TestCase):
    gumball_machine = gumball_machine_class.GumballMachine()

    def test_dispense_red(self):
        """Tests dispensing a red gumball with no money in the machine"""
        # input: dispense_red()
        expected_output = "You need at least 5 cents to dispense a red gumball"

        actual_output = self.gumball_machine.dispense_red()
        self.assertEqual(expected_output, actual_output)

    def test_dispense_yellow(self):
        """Tests dispensing a yellow gumball with no money in the machine"""
        # input: dispense_yellow()
        expected_output = "You need at least 10 cents to dispense a yellow gumball"

        actual_output = self.gumball_machine.dispense_yellow()
        self.assertEqual(expected_output, actual_output)

    def test_return_my_change(self):
        """Tests returning change with no money in the machine"""
        # input: return_my_change()
        expected_output = "There is no change to return"

        actual_output = self.gumball_machine.return_my_change()
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()
