from AoC2015.Day6 import Day6, Grid
from AdventUtils.Grid2D import Grid2DBool
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("turn on 0,0 through 999,999", [('on', (0, 0), (999, 999))]),
    ("toggle 0,0 through 999,0", [('toggle', (0, 0), (999, 0))]),
    ("turn off 5,15 through 10,20", [('off', (5, 15), (10, 20))]),

])
def test_parse_content(test_input, expected):
    d = Day6(content="test")
    assert d.parse_content(test_input) == expected


def test_apply():
    instr = [('on', (0, 10), (0, 15))]
    grid: Grid = Grid2DBool()
    grid = Day6(content='turn on 0,10 through 0,15').apply(instr, grid)
    assert not grid.grid.get((0, 9))
    assert grid.grid.get((0, 10))
    assert grid.grid.get((0, 11))
    assert grid.grid.get((0, 12))
    assert grid.grid.get((0, 13))
    assert grid.grid.get((0, 14))
    assert grid.grid.get((0, 15))
    assert not grid.grid.get((0, 16))
    assert not grid.grid.get((1, 13))
