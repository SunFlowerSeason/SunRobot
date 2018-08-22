import sys
from Robot import Robot, RobotException
from Command import Command, CommandException
from Compass import CompassHeadingException

class Application(object):
    @staticmethod
    def Process():
        toy = Robot()
        try:
            print("\n")
            print("Welcome to the Toy Robot application.\n")
            print("Proceed to enter commands. Press CTRL-C to exit.\n")
          # Loop until we receive a kill signal.
            while True:
              # BUG: Change to input() for Python 3.x
                line = raw_input("> ")
                try:
                  # Parse the command.
                    cmd = Command(line)
                  # Pass the validated command to the robot for actioning.
                    toy.Process(cmd)
                except CommandException as ce:
                    print(ce)
                except RobotException as re:
                    print(re)
                except CompassHeadingException as he:
                    print(he)
        except KeyboardInterrupt as kb:
            print("Keyboard exit signal detected.")
            pass
        finally:
            print("Exit requested.")
            toy.Cleanup()
            print("Application successfully exited.")
        return

# Entry point.        
if __name__ == '__main__':
    for arg in sys.argv:
        if arg == "-h": # Print a help screen.
            print("The Toy Robot application accepts single commands on the command prompt.\n")
            print("Supported commands include:\n")
            print("PLACE X,Y,D - Places the toy robot on the field at the coordinate X and Y and eading D (N, S, E, or W).\n")
            print("MOVE - Moves the robot forward one unit in it's current heading.\n")
            print("TURN D - Turns the robot to a new heading D (N, S, E, or W).\n")
            print("REPORT - Console print out of the robot's current location and it's heading.\n")
        if arg == "-a": # Print an about screen.
            print("The Toy Robot application was authored by Simon Flannery, August 2018.\n")

    Application.Process()
