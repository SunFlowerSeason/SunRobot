from Command import Command
from Compass import CompassHeadingException, ValidateCompassHeading, PrintCompassHeading

# Setup a few specific exceptions.
class RobotException(Exception):
    pass
    
class BoundsException(Exception):
    pass

# A simple class interface.
class Android(object):
    def __init__(self, obj):
        self._obj = obj

    def Reset(self):
        raise NotImplementedError
        return

    def Process(self):
        raise NotImplementedError
        return

    def Print(self):
        raise NotImplementedError
        return

    def Cleanup(self):
        raise NotImplementedError
        return

# A simple robot class inherited from the Android class. The robot class maintains it's own
# state information including X and Y positioning, field demensions, and compass heading.
# Except for the Print member function, please do not print logs in this class.
# All printing needs are handled external to this class by raising specific exceptions.
class Robot(Android):
    MAX_FIELD_X = 10
    MAX_FIELD_Y = 10

    def __init__(self):
        self.Reset()

    def __str__(self):
        self.Print()
        return

    def Reset(self):
        self.x = 0
        self.y = 0
        self.max_x = self.MAX_FIELD_X
        self.max_y = self.MAX_FIELD_Y
        self.heading = 'N'
        self.is_placed = False
        return

  # Position (0, 0) is the lower left corner of the field.
    def Place(self, start_x = 0, start_y = 0, heading = 'N'):
        if ValidateCompassHeading(heading) != False:
            if start_x >= 0 and start_x < self.max_x:
                if start_y >= 0 and start_y < self.max_y: 
                    self.x = start_x
                    self.y = start_y
                    self.heading = heading
                    self.is_placed = True
                else:
                    raise RobotException("Error. Invalid Y starting position [%d] for PLACE command. Y starting position exceeds bounds [%d, %d]." % (start_y, 0, max_y))
            else:
                raise RobotException("Error. Invalid X starting position [%d] for PLACE command. X starting position exceeds bounds [%d, %d]." % (start_x, 0, max_x))
        else:
            raise CompassHeadingException("Error. Invalid compass heading for PLACE command.")
        return

  # Prevent the robot from exceeding it's field.
  # Does not raise an exception if the robot is commanded to escape.
    def __Restrict(self):
        if self.y < 0:
            self.y = 0
        elif self.y >= self.max_y:
            self.y = self.max_y - 1
        if self.x < 0:
            self.x = 0
        elif self.x >= self.max_x:
            self.x = self.max_x - 1
        return
        
    def Move(self):
        if self.IsPlaced() != False:
            if self.heading == 'N':
                self.y = self.y + 1
            elif self.heading == 'E':
                self.x = self.x + 1
            elif self.heading == 'S':
                self.y = self.y - 1
            elif self.heading == 'W':
                self.x = self.x - 1
            self.__Restrict()
        else:
            raise RobotException("Error. Toy Robot not placed. Ignoring MOVE command.")
        return

    def Turn(self, h = 'N'):
        if self.IsPlaced() != False:
            if ValidateCompassHeading(h) != False:
                self.heading = h
            else:
                raise RobotException("Error. Invalid compass heading for TURN command.")
        else:
            raise RobotException("Error. Toy Robot not placed. Ignoring TURN command.")
        return

    def Process(self, cmd):
        tokens = cmd.GetCommand()
        if tokens[0] == "PLACE":
            self.Place(tokens[2], tokens[3], tokens[1])
        elif tokens[0] == "MOVE":
            self.Move()
        elif tokens[0] == "TURN":
            self.Turn(tokens[1])
        elif tokens[0] == "REPORT":
            self.Print()
        else:
            raise RobotException("Error. Ignoring unknown command %s." % tokens[0])
        return

    def Print(self):
        if self.IsPlaced() != False:
            print_heading = PrintCompassHeading(self.heading)
            print("The Toy Robot is at position %d,%d facing %s" % (self.x, self.y, print_heading))
        else:
            raise RobotException("Error. Toy Robot not placed. Ignoring REPORT command.")
        return

    def GetPosition(self):
        return self.x, self.y, self.heading

    def IsPlaced(self):
        return self.is_placed

    def Cleanup(self):
      # Nothing to clean up.
        return
