import constants
from game.casting.actor1 import Actor1
from game.shared.point import Point


class Player1(Actor1):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        
        self._segments.append(self._segments[0].copy())
        self._segments[-1].set_velocity(Point(0, 0))
        self._segments[-1].set_text("#")
        self._segments[0].move_next()
        
    
    def get_head(self):
        return self._segments[0]


    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.CELL_SIZE*2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor1()
            segment.set_position(position)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)