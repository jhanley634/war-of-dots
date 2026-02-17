import unittest

from constants import CELL_SIZE
from wod_server import Environment, MarchingSquares, City
from unittest.mock import patch, MagicMock


def gen_terrain(env: Environment) -> None:
    albany = City((3 * CELL_SIZE, 4 * CELL_SIZE))
    boston = City((5 * CELL_SIZE, 6 * CELL_SIZE))
    env.cities += [albany, boston]


class Test(unittest.TestCase):

    def test_get_grid_value(self) -> None:
        ms = MarchingSquares()
        self.assertAlmostEqual(0.0, ms.get_grid_value(5.0, 6.0))

    @staticmethod
    def _gen_environment() -> Environment:
        env = Environment()
        f = env.forest_marching
        f.grid[3][4] = 0.92
        f.grid[4][4] = 0.96
        t = env.terrain_marching
        t.grid[3][4] = 0.91
        t.grid[4][4] = 0.95
        env.generate_default_vision()
        return env

    def _check_marching(self, env: Environment) -> None:
        self.assertAlmostEqual(0.7424, env.forest_marching.get_grid_value(3.2, 4.2))

        self.assertAlmostEqual(0.7344, env.terrain_marching.get_grid_value(3.2, 4.2))

    def _check_vision(self, env: Environment) -> None:
        v = env.default_vision
        self.assertAlmostEqual(2.15, v[3][4])
        self.assertAlmostEqual(2.15, v[4][4])

        # It defaults to "poor visibility".
        self.assertAlmostEqual(0.65, v[5][4])
        self.assertAlmostEqual(0.65, v[0][0])

    def _check_draw(self, env: Environment) -> None:
        di = env.draw_info(player=0)
        self.assertEqual([], di[2])
        red, blue = 0, 1
        self.assertEqual(
            ((255, 0, 0), (60, 80)),
            di[3][red][:2],
        )
        self.assertEqual(
            ((0, 0, 255), (100, 120)),
            di[3][blue][:2],
        )

    @patch.object(Environment, "generate_terrain", autospec=True)
    def test_environment(self, mock_generate_terrain: MagicMock) -> None:
        # The Environment constructor calls self.generate_terrain(), which is random.
        # I need to mock it out, so we instead call a no-op function.
        mock_generate_terrain.side_effect = gen_terrain

        env = self._gen_environment()
        self.assertEqual(2, len(env.cities))
        self.assertEqual((60, 80), env.cities[0].position)

        self._check_marching(env)
        self._check_vision(env)
        self._check_draw(env)
