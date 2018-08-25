from Compass import CompassHeadingException, Compass
from Robot import Robot

class CommandException(Exception):
    pass

class CommandAction(object):
    def __init__(self):
        pass

    def Execute(self):
        raise NotImplementedError
        return

class CommandMove(CommandAction):
    def __init__(self):
        super(CommandMove, self).__init__()

    def Execute(self, bot):
        bot.Move()
        return

class CommandReport(CommandAction):
    def __init__(self):
        super(CommandReport, self).__init__()
        pass

    def Execute(self, bot):
        bot.Print()
        return

class CommandTurn(CommandAction):
    def __init__(self, heading):
        super(CommandTurn, self).__init__()
        self.heading = heading
        pass

    def Execute(self, bot):
        bot.Turn(self.heading)
        return

    def GetHeading(self):
        return self.heading

class CommandPlace(CommandTurn):
    def __init__(self, x, y, heading):
        super(CommandPlace, self).__init__(heading)
        self.x = x
        self.y = y

    def Execute(self, bot):
        bot.Place(self.x, self.y, self.heading)
        return

    def GetPosition(self):
        return self.x, self.y

# A dedicated class to handle the parsing of string commands. The commands could be passed
# from a file or via the console prompt.
# Please do not print logs in this class. All printing needs are handled external to
# this class by raising specific exceptions.
class Command(object):
    def __init__(self, args):
        self.Parse(args)

    def GetCommand(self):
        return self.instruction
        
    def Parse(self, args):
        self.instruction = None
      # Convert the entire command to uppercase.
        args = args.upper()
      # Replace commas with a whitespace token to ease parsing.
        args = args.replace(',', ' ')
        command = args.split()
        if command[0] == "MOVE":
             if len(command) == 1:
                 self.instruction = CommandMove()
             else:
                 raise CommandException("Error. Too many parameters for MOVE command.")
        elif command[0] == "REPORT":
            if len(command) == 1:
                self.instruction = CommandReport()
            else:
                raise CommandException("Error. Too many parameters for REPORT command.")
        elif command[0] == "TURN":
            if len(command) == 2:
                if Compass.ValidateHeading(command[1]) != False:
                    self.instruction = CommandTurn(command[1])
                else:
                    raise CompassHeadingException("Error. Invalid compass heading for TURN command.")
            elif len(command) < 2:
                raise CommandException("Error. Too few parameters for TURN command.")
            elif len(command) > 2:
                raise CommandException("Error. Too many parameters for TURN command.")
        elif command[0] == "PLACE":
            if len(command) == 4:
                if command[1].isdigit() == False:
                    raise CommandException("Error. Invalid X starting position [%s] for PLACE command." % (command[1]))
                if command[2].isdigit() == False:
                    raise CommandException("Error. Invalid Y starting position [%s] for PLACE command." % (command[2]))
                if Compass.ValidateHeading(command[3]) != False:
                    self.instruction = CommandPlace(int(command[1]), int(command[2]), command[3])
                else:
                    raise CompassHeadingException("Error. Invalid compass heading for PLACE command.")
            elif len(command) < 4:
                raise CommandException("Error. Too few parameters for PLACE command.")
            elif len(command) > 4:
                raise CommandException("Error. Too many parameters for PLACE command.")
        else:
            raise CommandException("Error. Unknown command %s to parse." % command[0])
        return

    def Execute(self, bot):
        if bot != None:
            self.instruction.Execute(bot)
        return
