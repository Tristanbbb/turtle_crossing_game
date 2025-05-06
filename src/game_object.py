from turtle import Turtle

# Class inheriting from Turtle, and from which Car and Player are inheriting

class GameObject(Turtle):
    def __init__(self):
        super().__init__()
        self.up()

        # Hitbox coordinates
        self.hitbox_top = None
        self.hitbox_bottom = None
        self.hitbox_left = None
        self.hitbox_right = None

    def refresh_hitbox_coordinates(self, hitbox_dict):
        self.hitbox_top = round(self.ycor() + hitbox_dict['top'],1)
        self.hitbox_bottom = round(self.ycor() + hitbox_dict['bottom'],1)
        self.hitbox_left = round(self.xcor() + hitbox_dict['left'],1)
        self.hitbox_right = round(self.xcor() + hitbox_dict['right'],1)

    # For debugging
    def print_hitbox_coordinates(self):
        print(type(self))
        print(f"""
              TOP={self.hitbox_top}
        LEFT={self.hitbox_left}        RIGHT={self.hitbox_right}
              BOTTOM={self.hitbox_bottom}
        """)