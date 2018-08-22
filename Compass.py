class CompassHeadingException(Exception):
    pass

# A utility function to validate the heading of a compass.
# This function would be used to support both the Command and Robot classes.
# Adding new compass headings would only need to update this single function.
def ValidateCompassHeading(h):
    return h in ['N', 'E', 'S', 'W']

def PrintCompassHeading(h):
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
