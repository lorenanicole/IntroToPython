import sys

libDir = "LearnWithLlew.jar"
sys.path.append(libDir)

from org.learnwithllew.teachingextensions.logo import Colors


def get_random_color():
    return Colors.getRandomColor()

class Reds(object):
    Red = Colors.Reds.Red
class Blues(object):
    Blue = Colors.Blues.Blue
class Yellows(object):
    Yellow = Colors.Yellows.Yellow