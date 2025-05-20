import os
import json
import config


class Scoreboard:
    def __init__(self, scores_file_path=None):
        self.scores_file_path = scores_file_path
        self.scores_list = [] # Initialized in initialize_saved_scores()
        self.try_initialize_scores_file()
        self.initialize_saved_scores()

    # Function to create the file if it doesn't exist
    def try_initialize_scores_file(self):
        if not os.path.isfile(self.scores_file_path) or os.stat(self.scores_file_path).st_size == 0:
            with open(self.scores_file_path, 'w') as f:
                json.dump([], f)

    def order_and_pop_scores(self):
        try:
            print(self.scores_list)
            print("\n\n")
            self.scores_list = [score for score in self.scores_list if score['level'] is not None and score['time'] is not None]
            print(self.scores_list)
            #print(f'self.scores_list : {self.scores_list}')
            self.scores_list = sorted(self.scores_list, key=lambda x: (x['level'], -x['time']), reverse=True)  #reverse=True
            self.scores_list = self.scores_list[:config.MAX_SCORES_SAVED] # Storing only the nb of scores set in the configuration.
            #print(f'self.scores_list[:config.MAX_SCORES_SAVED] = {self.scores_list[:config.MAX_SCORES_SAVED]}')
        except KeyError as e:
            print(f"KeyError in order_and_pop_scores(): {e}")
            print("Verify the json file")
        except TypeError as e:
            print(f"TypeError in order_and_pop_scores(): {e}")
            print("Score not saved.")

    # Function retrieving the saved scores from the file
    def initialize_saved_scores(self):
        try:
            with open(self.scores_file_path, "r") as scores_file:
                self.scores_list = json.load(scores_file)
        except FileNotFoundError:
            print("Scoreboard file not found. It will be created at the end of this game.")

    def get_top_level(self):
        try:
            return self.scores_list[0]
        except IndexError:  # If no score we return None
            return None

    def save_score(self, score):
        # If the directory doesn't exist, we create it
        # exist_ok=True => "if the directory already exist, don't raise an exception"
        os.makedirs(os.path.dirname(self.scores_file_path), exist_ok=True)

        # Adding the score to the list
        self.scores_list.append(score)
        # Reordering the list and popping the scores after the 3rd rank
        self.order_and_pop_scores()

        # Saving the list to the file
        with open(self.scores_file_path,"w") as file:
            file.write(json.dumps(self.scores_list, indent=4))

