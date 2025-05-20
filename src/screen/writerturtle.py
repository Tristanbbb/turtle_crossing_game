import config
from turtle import Turtle

class WriterTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()

# The turtle writing the score and also displaying the top score for comparison
class ScoreWriterTurtle(WriterTurtle):
    def __init__(self):
        super().__init__()

    # Wrapper method for the 2 methods below
    def write_current_level_and_top_level(self, current_level:int, top_level:int):
        self.write_level(current_level)
        if top_level is not None:
            self.write_top_score(top_level)

    def write_level(self, current_level: int):
        self.goto(-config.SCREEN_WIDTH / 2 + 70, config.SCREEN_HEIGHT / 2 - 30)
        self.clear()
        self.write(arg=f"Level {current_level}",
                          align="center", move=False, font=config.FONT_CURRENT_LEVEL)

    def write_top_score(self, top_level: int):
        self.goto(config.SCREEN_WIDTH / 2 - 100, config.SCREEN_HEIGHT / 2 - 30)
        self.clear()
        self.write(arg=f"Level to beat: {top_level['level']}",
                   align="center", move=False, font=config.FONT_TOP_LEVEL)

class GameOverWriterTurtle(WriterTurtle):
    def __init__(self):
        super().__init__()
        self.color("red")

    def write_game_over(self, level: int, time_to_level:float):
        self.write("GAME OVER",align= 'center', font=config.FONT_GAME_OVER)
        self.goto(0, -30)
        self.write(f"Your final level: {level}",
                                    align= 'center',
                                    font=config.FONT_GAME_OVER)
        if time_to_level:
            self.goto(0, -60)
            self.write(f"Time to reach level: {round(time_to_level,4)} seconds",
                                        align='center',
                                        font=config.FONT_GAME_OVER)
