import unittest
import gumball_machine as gumball_machine_class


class NoMoneyTestCases(unittest.TestCase):
    gumball_machine = gumball_machine_class.GumballMachine()

    def test_dispense_red(self):
        response = self.gumball_machine.dispense_red()
        self.assertEqual(response, "You need at least 5 cents to dispense a red gumball")

    def test_dispense_yellow(self):
        response = self.gumball_machine.dispense_yellow()
        self.assertEqual("You need at least 10 cents to dispense a yellow gumball", response)

    def test_return_my_change(self):
        response = self.gumball_machine.return_my_change()
        self.assertEqual("There is no change to return", response)


if __name__ == '__main__':
    unittest.main()
