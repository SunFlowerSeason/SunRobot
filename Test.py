import unittest
from Robot import Robot, RobotException
from Command import Command, CommandException
from Compass import CompassHeadingException

class CommmandTestCases(unittest.TestCase):
    def test_positive_command_1(self):
        cmd = Command("MOve   ")
        self.assertEqual(cmd.GetCommand()[0], "MOVE")
        return

    def test_positive_command_2(self):
        cmd = Command("rePORt")
        self.assertEqual(cmd.GetCommand()[0], "REPORT")
        return

    def test_positive_command_3(self):
        cmd = Command("tuRn   w")
        self.assertEqual(cmd.GetCommand()[0], "TURN")
        self.assertEqual(cmd.GetCommand()[1], "W")
        return

    def test_positive_command_4(self):
        cmd = Command("place 1,2,E")
        self.assertEqual(cmd.GetCommand()[0], "PLACE")
        self.assertEqual(cmd.GetCommand()[2], 1)
        self.assertEqual(cmd.GetCommand()[3], 2)
        self.assertEqual(cmd.GetCommand()[1], "E")
        return

    def test_positive_command_5(self):
        cmd = Command("plACe 0    2   N")
        self.assertEqual(cmd.GetCommand()[0], "PLACE")
        self.assertEqual(cmd.GetCommand()[2], 0)
        self.assertEqual(cmd.GetCommand()[3], 2)
        self.assertEqual(cmd.GetCommand()[1], "N")
        return

    def test_negative_command_1(self):
        self.assertRaises(CommandException, Command, "Hello World")
        return

    def test_negative_command_2(self):
        self.assertRaises(CompassHeadingException, Command, "Place 0 0 Q")
        return

class RobotTestCases(unittest.TestCase):
    def test_positive_robot_1(self):
        bot = Robot()
        bot.Process(Command("place 1,1,N"))
        self.assertEqual(bot.IsPlaced(), True)
        return

    def test_positive_robot_2(self):
        bot = Robot()
        bot.Process(Command("place 3,2,E"))
        bot.Process(Command("MOVE"))
        self.assertEqual(bot.IsPlaced(), True)
        self.assertEqual(bot.GetPosition()[0], 4)
        self.assertEqual(bot.GetPosition()[1], 2)
        self.assertEqual(bot.GetPosition()[2], "E")
        return

    def test_positive_robot_3(self):
        bot = Robot()
        bot.Process(Command("place 3 2 W"))
        bot.Process(Command("MOVE"))
        bot.Process(Command("MOVE"))
        bot.Process(Command("MOVE"))
        bot.Process(Command("MOVE"))
        bot.Process(Command("MOVE"))
        bot.Process(Command("MOVE"))
        bot.Process(Command("MOVE"))
        self.assertEqual(bot.IsPlaced(), True)
        self.assertEqual(bot.GetPosition()[0], 0)
        self.assertEqual(bot.GetPosition()[1], 2)
        self.assertEqual(bot.GetPosition()[2], "W")
        return

    def test_negative_robot_1(self):
        bot = Robot()
        self.assertRaises(RobotException, bot.Process, Command("Move  "))
        self.assertEqual(bot.IsPlaced(), False)
        return

# Test entry point.        
if __name__ == '__main__':
    unittest.main()
