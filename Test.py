import unittest
from Robot import Robot, RobotException
from Command import Command, CommandException, CommandMove, CommandReport, CommandTurn, CommandPlace
from Compass import Compass, CompassHeadingException

class CommmandTestCases(unittest.TestCase):
    def test_positive_command_1(self):
        cmd = Command("MOve   ")
        self.assertIsInstance(cmd.GetCommand(), CommandMove)
        return

    def test_positive_command_2(self):
        cmd = Command("rePORt")
        self.assertIsInstance(cmd.GetCommand(), CommandReport)
        return

    def test_positive_command_3(self):
        cmd = Command("tuRn   w")
        self.assertIsInstance(cmd.GetCommand(), CommandTurn)
        self.assertEqual(cmd.GetCommand().GetHeading(), "W")
        return

    def test_positive_command_4(self):
        cmd = Command("place 1,2,E")
        self.assertIsInstance(cmd.GetCommand(), CommandPlace)
        self.assertEqual(cmd.GetCommand().GetPosition()[0], 1)
        self.assertEqual(cmd.GetCommand().GetPosition()[1], 2)
        self.assertEqual(cmd.GetCommand().GetHeading(), "E")
        return

    def test_positive_command_5(self):
        cmd = Command("plACe 0    2   N")
        self.assertIsInstance(cmd.GetCommand(), CommandPlace)
        self.assertEqual(cmd.GetCommand().GetPosition()[0], 0)
        self.assertEqual(cmd.GetCommand().GetPosition()[1], 2)
        self.assertEqual(cmd.GetCommand().GetHeading(), "N")
        return

    def test_negative_command_1(self):
        self.assertRaises(CommandException, Command, "Hello World")
        return

    def test_negative_command_2(self):
        self.assertRaises(CompassHeadingException, Command, "Place 0 0 Q")
        return

class CompassTestCases(unittest.TestCase):
    def test_positive_compass_1(self):
        self.assertEqual(Compass.ValidateHeading("N"), True)
        return

    def test_positive_compass_2(self):
        self.assertEqual(Compass.ValidateHeading("V"), False)
        return

class RobotTestCases(unittest.TestCase):
    def test_positive_robot_1(self):
        bot = Robot()
        Command("place 1,1,N").Execute(bot)
        self.assertEqual(bot.IsPlaced(), True)
        return

    def test_positive_robot_2(self):
        bot = Robot()
        self.assertEqual(bot.IsPlaced(), False)
        return

    def test_positive_robot_3(self):
        bot = Robot()
        Command("place 3,2,E").Execute(bot)
        Command("MOVE").Execute(bot)
        self.assertEqual(bot.IsPlaced(), True)
        self.assertEqual(bot.GetPosition()[0], 4)
        self.assertEqual(bot.GetPosition()[1], 2)
        self.assertEqual(bot.GetPosition()[2], "E")
        return

    def test_positive_robot_4(self):
        bot = Robot()
        Command("place 3 2 W").Execute(bot)
        Command("MOVE").Execute(bot)
        Command("MOVE").Execute(bot)
        Command("MOVE").Execute(bot)
        Command("MOVE").Execute(bot)
        Command("MOVE").Execute(bot)
        Command("MOVE").Execute(bot)
        Command("MOVE").Execute(bot)
        self.assertEqual(bot.IsPlaced(), True)
        self.assertEqual(bot.GetPosition()[0], 0)
        self.assertEqual(bot.GetPosition()[1], 2)
        self.assertEqual(bot.GetPosition()[2], "W")
        return

    def test_negative_robot_1(self):
        bot = Robot()
        self.assertRaises(RobotException, Command("Move  ").Execute, bot)
        return

# Test entry point.        
if __name__ == '__main__':
    unittest.main()
