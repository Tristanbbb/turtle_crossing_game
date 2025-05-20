import os
import unittest
from src.score.scoreboard import Scoreboard

class ScoreboardTest(unittest.TestCase):

    def setUp(self):
        self.scoreboard = Scoreboard("./data/scores_test_order_and_pop_scores.json")
        self.scoreboard.try_initialize_scores_file()

    def tearDown(self):
        os.remove("./data/scores_test_order_and_pop_scores.json")

    def test_save_scores(self):
        score_to_save = {
            "player": "Tristan",
            "level": 6,
            "time": 5.38
        }
        self.scoreboard.save_score(score_to_save)
        print(self.scoreboard.scores_list)
        score_to_save = {
            "player": "Tamara",
            "level": 7,
            "time": 6.15
        }
        self.scoreboard.save_score(score_to_save)
        print(self.scoreboard.scores_list)
        score_to_save = {
            "player": "Greg",
            "level": 4,
            "time": 125
        }
        self.scoreboard.save_score(score_to_save)
        print(self.scoreboard.scores_list)
        score_to_save = {
            "player": "Alina",
            "level": 7,
            "time": 7.25
        }
        self.scoreboard.save_score(score_to_save)
        print(self.scoreboard.scores_list)
        score_to_save = {
            "player": "Alina",
            "level": 1,
            "time": None
        }
        self.scoreboard.save_score(score_to_save)
        print(self.scoreboard.scores_list)

