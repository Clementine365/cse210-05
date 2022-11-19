import constants
from game.casting.actor1 import Actor1
from game.casting.actor2 import Actor2
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the players collides
    with the other player or with him or herself or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
        _winner(string): tells who the winner is
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ""
        

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
        """Sets the game over flag if the players collides with one of its segments or
           collides with each other.
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
            # player1 collides with himself
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "Player2 won!"
               
            # player2 collides with player1
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "Player1 won!"
                   
        for segment in segment2:
            # player1 collides with player2
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "Player2 won!"
                
            # player2 collides with himself
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = "Player1 won!"
                
        # player1 and player2 collides head on
        if head1.get_position().equals(head2.get_position()):
                self._is_game_over = True
                self._winner = "It's a tie!"
                     
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the player1 and player2 white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("player1s")
            segment1 = player1.get_segments()

            player2 = cast.get_first_actor("player2s")
            segment2 = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            # game over message handling
            message = Actor1() 
            message.set_text(f"Game Over! {self._winner}")
            message.set_color(Color(255, 0, 0))
            message.set_position(position)
            cast.add_actor("messages", message)

            # change player1 to be white
            for segment in segment1:
                segment.set_color(constants.WHITE)

            # change player2 to be white
            for segment in segment2:
                segment.set_color(constants.WHITE)   