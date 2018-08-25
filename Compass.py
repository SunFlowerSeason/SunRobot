class CompassHeadingException(Exception):
    pass

# A utility module to validate the heading of a compass.
# This module would be used to support both the Command and Robot classes.
# Adding new compass headings would only need to update these single member functions.
class Compass(object):
    @staticmethod
    def ValidateHeading(h):
        return h in ['N', 'E', 'S', 'W']

    @staticmethod
    def PrintHeading(h):
        heading = "Unknown"
        if h == 'N':
            heading = "North"
        elif h == 'E':
            heading = "East"
        elif h == 'S':
            heading = "South"
        elif h == 'W':
            heading = "West"
        return heading
