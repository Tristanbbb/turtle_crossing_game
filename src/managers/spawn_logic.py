from enum import Enum, auto

# Used as an attribute of CarManager
# The policy is that either all cars spawn on the right, or they spawn on both sides
class SpawnPolicy(Enum):
    # Using "auto()" because we don't care about the actual values, so no need to set the values to 1 and 2.
    RIGHT = auto()
    BOTH = auto()

# Called while initializing a new instance of Car
# Either the car spawns on the left, or on the right
class SpawnSide(Enum):
    # Using "auto()" because we don't care about the actual values, so no need to set the values to 1 and 2.
    LEFT = auto()
    RIGHT = auto()