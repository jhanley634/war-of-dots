import unittest

from wod_server import MarchingSquares


class Test(unittest.TestCase):

    def test_get_grid_value(self) -> None:
        ms = MarchingSquares()
        self.assertAlmostEqual(0.0, ms.get_grid_value(5.0, 6.0))
