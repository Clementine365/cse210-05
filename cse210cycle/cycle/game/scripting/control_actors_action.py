import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the player's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction1 = Point(constants.CELL_SIZE, 0)
        self._direction2 = Point(-constants.CELL_SIZE, 0)
    

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left for player1
        if self._keyboard_service.is_key_down('a'): 
            self._direction1 = Point(-constants.CELL_SIZE, 0)
            
        
        # right for player1
        if self._keyboard_service.is_key_down('d'):
            self._direction1 = Point(constants.CELL_SIZE, 0) 
                
        # up for player1
        if self._keyboard_service.is_key_down('w'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
        
        # down for player1
        if self._keyboard_service.is_key_down('s'):
            self._direction1 = Point(0, constants.CELL_SIZE)
        
        player1 = cast.get_first_actor("player1s")
        player1.turn_head(self._direction1)

    
        # left for player2
        if self._keyboard_service.is_key_down('j'): 
            self._direction2 = Point(-constants.CELL_SIZE, 0) 

        # right for player2
        if self._keyboard_service.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0) 

        # up for player2
        if self._keyboard_service.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)

        # down for player2
        if self._keyboard_service.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)

        player2 = cast.get_first_actor("player2s")
        player2.turn_head(self._direction2)    