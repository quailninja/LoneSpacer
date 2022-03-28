
from game.scripting.action import Action
from game.casting.health_bar import HealthBar
from game.casting.level import Level
from game.casting.score import Score

class HUD(Action):
    
    def execute(self, cast):
        health = cast.get_actors(HealthBar)
        level = cast.get_actors(Level)
        score = cast.get_actors(Score)
