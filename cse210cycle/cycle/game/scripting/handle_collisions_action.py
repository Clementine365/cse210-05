import constants
from game.casting.actor1 import Actor1
from game.casting.actor2 import Actor2
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("player1s")
        head1 = player1.get_segments()[0]
        segment1 = player1.get_segments()[1:]

        player2 = cast.get_first_actor("player2s")
        head2 = player2.get_segments()[0]
        segment2 = player2.get_segments()[1:]
    
        
        for segment in segment1:
            if head1.get_position().equals(segment.get_position()) \
                or head2.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in segment2:
            if head1.get_position().equals(segment.get_position()) \
                or head2.get_position().equals(segment.get_position()):
                self._is_game_over = True        
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("player1s")
            segment1 = player1.get_segments()
            #food = cast.get_first_actor("foods")

            player2 = cast.get_first_actor("player2s")
            segment2 = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor1()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segment1:
                segment.set_color(constants.WHITE)

            for segment in segment2:
                segment.set_color(constants.WHITE)    
            #food.set_color(constants.WHITE)