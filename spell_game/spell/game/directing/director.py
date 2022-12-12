from game.casting.artifact import Artifact
from game.shared.color import Color

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._points = 0 #to keep track of overall score
        # self._size = 15
        self.artifact = Artifact()

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the spider.
        
        Args:
            cast (Cast): The cast of actors.
        """
        spider = cast.get_first_actor("spiders")
        velocity = self._keyboard_service.get_direction()
        spider.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the spider's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        # moved to handle_collisions_artifact?
        banner = cast.get_first_actor("banners")
        lives = cast.get_first_actor('lives')
        end_title = cast.get_first_actor('end')
        spider = cast.get_first_actor("spiders")
        artifacts = cast.get_actors("artifacts") #list of artifacts 
        artifact = Artifact()
        self._is_game_over = False
        spell_effect = 'CURSED'

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        spider.move_next(max_x, max_y)


        # while self._is_game_over == False:
        if not self._is_game_over == True:

            for artifact in artifacts: #loop through each artifact in the list. 
                if spider.get_position().equals(artifact.get_position()): 
                    self._points = self._points + artifact.calculate_points()
                    cast.remove_actor('artifacts', artifact)

                artifact.move_next(max_x, max_y)
                banner.set_text(f'Score: {self._points}') #shows current points on screen
                lives.set_text(f'Spell: {spell_effect}') 

                # if self._points < 0: #end game if there are no points
                if self._points % 2 == 1:
                    self._is_game_over = True
                    # director._end_game()
                    spell_effect = 'FROZEN'
                    WHITE = Color(255, 255, 255)
                    spider.set_color(WHITE)
                    artifact.set_color(WHITE)
                    lives.set_text(f'Spell: {spell_effect}') #change the print
                    break # this causes the pause in all items but 1 until if statment is wrong
                # if self._points > 100:
                #     end_title.set_text('YAY, you won!\nPlay again?')
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    # def _do_end_game(self, cast):
    #     """What happends when the game ends           
    #     """

            
        