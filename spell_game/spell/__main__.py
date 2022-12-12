import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


#import constants
#move to constance
FRAME_RATE = 15
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Spell"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    _banner = Actor()
    _banner.set_text('Score: ')
    _banner.set_font_size(FONT_SIZE)
    _banner.set_color(WHITE)
    _banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create spell
    lives = Actor()
    lives.set_text('Lives: ')
    lives.set_color(WHITE)
    lives.set_position(Point(CELL_SIZE, 25)) #where it promts on the screen
    cast.add_actor("lives", lives)
 
    # # end_title = cast.get_first_actor('end')
    # end_title = Actor()
    # end_title.set_text('YAY, you won!\nPlay again?')
    # end_title.set_color(WHITE)
    # end_title.set_position(Point(CELL_SIZE, 25)) #where it promts on the screen
    # cast.add_actor("end_title", end_title)
    
    
    # create the spider
    x = int(MAX_X / 2)
    position = Point(x, MAX_Y - 20)

    spider = Actor()
    spider.set_text("U\nW")
    spider.set_font_size(FONT_SIZE)
    spider.set_color(WHITE)
    spider.set_position(position)
    cast.add_actor("spiders", spider)

    #creates flies and rocks
    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(['}{', 'O']) # '}{' is fly. 'O' is rock

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
   
        #choose random color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)        

        if text == 'O':
            artifact.set_velocity(Point(0, 1)) # x= 0 x axis stays , y = 1 y moves ** This gives a static decent of all objects #original
        else:
            artifact.set_velocity(Point(0, random.randint(1, 2))) #varies object decent from 1 - 5 randomly , how can I make it choose 1 or 5 not inbetween?***********

        # artifact.set_velocity(Point(0, random.randint(1, 2)).scale(CELL_SIZE)) this makes it faster but nothing hits

        cast.add_actor("artifacts", artifact)

        # artifact.set_velocity(Point(0, 1).scale(CELL_SIZE))      # Velocity is one cell down

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast) 


if __name__ == "__main__":
    main()

