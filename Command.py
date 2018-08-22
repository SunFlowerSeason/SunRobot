from Compass import CompassHeadingException, ValidateCompassHeading

class CommandException(Exception):
    pass

# A dedicated class to handle the parsing of string commands. The commands could be passed
# from a file or via the console prompt.
# Please do not print logs in this class. All printing needs are handled external to
# this class by raising specific exceptions.
class Command(object):
    def __init__(self, args):
        self.Parse(args)

    def GetCommand(self):
        return self.command, self.heading, self.x, self.y

    def Reset(self):
        self.command = "UNKNOWN"
        self.heading = "UNKNOWN"
        self.x = -1
        self.y = -1
        return
        
    def Parse(self, args):
        self.Reset()
      # Convert the entire command to uppercase.
        args = args.upper()
      # Replace commas with a whitespace token to ease parsing.
        args = args.replace(',', ' ')
        command = args.split()
        if command[0] == "MOVE":
             self.command = command[0]
             if len(command) > 1:
                 raise CommandException("Error. Too many parameters for MOVE command.")
        elif command[0] == "REPORT":
            self.command = command[0]
            if len(command) > 1:
                raise CommandException("Error. Too many parameters for REPORT command.")
        elif command[0] == "TURN":
            if len(command) == 2:
                if ValidateCompassHeading(command[1]) != False:
                    self.command = command[0]
                    self.heading = command[1]
                else:
                    raise CompassHeadingException("Error. Invalid compass heading for TURN command.")
            elif len(command) < 2:
                raise CommandException("Error. Too few parameters for TURN command.")
            elif len(command) > 2:
                raise CommandException("Error. Too many parameters for TURN command.")
        elif command[0] == "PLACE":
            if len(command) == 4:
                if command[1].isdigit() != False:
                    self.x = int(command[1])
                else:
                    raise CommandException("Error. Invalid X starting position [%s] for PLACE command." % (command[1]))
                if command[2].isdigit() != False:
                    self.y = int(command[2])
                else:
                    raise CommandException("Error. Invalid Y starting position [%s] for PLACE command." % (command[2]))
                if ValidateCompassHeading(command[3]) != False:
                    self.command = command[0]
                    self.heading = command[3]
                else:
                    raise CompassHeadingException("Error. Invalid compass heading for PLACE command.")
            elif len(command) < 4:
                raise CommandException("Error. Too few parameters for PLACE command.")
            elif len(command) > 4:
                raise CommandException("Error. Too many parameters for PLACE command.")
        else:
            raise CommandException("Error. Unknown command %s to parse." % command[0])
        return
