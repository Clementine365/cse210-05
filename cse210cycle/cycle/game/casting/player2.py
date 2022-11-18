import constants
from game.casting.actor2 import Actor2
from game.shared.point import Point


class Player2(Actor2):
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

    #def grow_tail(self, number_of_segments):
    #    for i in range(number_of_segments):
    #        tail = self._segments[-1]
    #        velocity = tail.get_velocity()
    #        offset = velocity.reverse()
    #        position = tail.get_position().add(offset)
    #        
    #        segment = Actor2()
    #        segment.set_position(position)
    #        segment.set_velocity(velocity)
    #        segment.set_text("#")
    #        segment.set_color(constants.GREEN)
    #        self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X - constants.CELL_SIZE*2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            #velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor2()
            segment.set_position(position)
            #segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)