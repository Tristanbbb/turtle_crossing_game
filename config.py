
# Game speed
REFRESH_INTERVAL = 0.1 # Refresh interval in seconds

# Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FINISH_LINE_Y = 299
FONT_CURRENT_LEVEL = ("Courier", 18, "normal")
FONT_TOP_LEVEL = ("Courier", 15, "normal")
FONT_GAME_OVER = ('Courier', 15, 'normal')

# Scoreboard
SCORES_FILE_PATH = "./data/scores.json"
MAX_SCORES_SAVED = 3

# Player configuration
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

# Player hitbox dimensions from center of the turtle
PLAYER_HITBOX = {
    'top': 17.0,
    'bottom': -9.0,
    'left': -10,
    'right': 10
}

# Car hitbox dimensions from center of the car
CAR_HITBOX = {
    'top': 10.0,
    'bottom': -10.0,
    'left': -20,
    'right': 20
}