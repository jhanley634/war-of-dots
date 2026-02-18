#! /usr/bin/env python


from constants import PLAYERS
from tests.marching_squares_test import DeterministicEnvironment
from wod_server import Game


class BenchmarkGame(Game):
    def game_logic(self):
        city_paths_to_apply = []
        for p_num in range(PLAYERS):
            if self.player_city_inputs[p_num]:
                city_paths_to_apply.extend(self.player_city_inputs[p_num])
        self.player_city_inputs = [[] for i in range(PLAYERS)]
        self.environment.update_cities(city_paths_to_apply)
        paths_to_apply = []
        for p_num in range(PLAYERS):
            if self.player_inputs[p_num]:
                paths_to_apply.extend(self.player_inputs[p_num])
        self.player_inputs = [[] for i in range(PLAYERS)]
        self.ready = False
        self.environment.update_troops(paths_to_apply)
        self.ready = True


def main() -> None:
    assert PLAYERS == 2
    game = BenchmarkGame()
    game.environment = DeterministicEnvironment()
    game.game_logic()


if __name__ == "__main__":
    main()
