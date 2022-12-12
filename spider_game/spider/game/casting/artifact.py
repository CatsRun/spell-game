import random
from game.casting.actor import Actor
# from game.shared.point import Point
import __main__

class Artifact(Actor):
    """Calculates points based on what object is gathered.

    This class is child to Actor class.

    Attributes:
        _position
    """
    def __init__(self):
        super().__init__()       
        self._main = __main__
        # self._point = Point()
        

    #artifact calculate score based on what it is
    def calculate_points(self):
        points = 0 #starting points

        if (self.get_text() == '}{'): 
            points = 5
        else:
            # points = -10 #end game or lose life
            points = random.randint(1 , 2)
        
        return points
