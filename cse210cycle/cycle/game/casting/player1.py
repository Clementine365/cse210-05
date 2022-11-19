import constants
from game.casting.actor1 import Actor1
from game.shared.point import Point


class Player1(Actor1):
    """
    A person who plays the game.
    
    The responsibility of Player1 is to move itself.

    Attributes:
        _segments(list): a list of a player1
    """
    def __init__(self):
        # Constructs Player1
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """Gets player1's segments
        Returns:
            segments(list): a list of player1
        """
        return self._segments

    def move_next(self):
        # Updates a next move of player1
        # add segments a copy of segments[0], which is a head
        self._segments.append(self._segments[0].copy())
        # turns off the velocity of the segments
        self._segments[-1].set_velocity(Point(0, 0))
        self._segments[-1].set_text("#")
        # head gets a new position
        self._segments[0].move_next()


    def turn_head(self, velocity):
        # head(segments[0]) gets new velocity
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        # initial setting of player1
        x = int(constants.MAX_X - constants.CELL_SIZE*2)
        y = int(constants.CELL_SIZE)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor1()
            segment.set_position(position)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)