from src.AdventUtils.Grid2D import Position2D, Grid2DBool, Grid2Dint
import pytest


@pytest.mark.parametrize("x, y, mag, ex_x, ex_y", [
    (0, 0, 1, 0, 1),
    (-1, -1, 1, -1, 0),
    (0, 0, 5, 0, 5)
])
def test_move_up(x, y, mag, ex_x, ex_y):
    assert Position2D(x, y).move_up(mag) == Position2D(ex_x, ex_y)


@pytest.mark.parametrize("x, y, mag, ex_x, ex_y", [
    (0, 0, 1, 0, -1),
    (-1, -1, 1, -1, -2),
    (0, 0, 5, 0, -5)
])
def test_move_down(x, y, mag, ex_x, ex_y):
    assert Position2D(x, y).move_down(mag) == Position2D(ex_x, ex_y)


@pytest.mark.parametrize("x, y, mag, ex_x, ex_y", [
    (0, 0, 1, -1, 0),
    (-1, -1, 1, -2, -1),
    (0, 0, 5, -5, 0)
])
def test_move_left(x, y, mag, ex_x, ex_y):
    assert Position2D(x, y).move_left(mag) == Position2D(ex_x, ex_y)


@pytest.mark.parametrize("x, y, mag, ex_x, ex_y", [
    (0, 0, 1, 1, 0),
    (-1, -1, 1, 0, -1),
    (0, 0, 5, 5, 0)
])
def test_move_right(x, y, mag, ex_x, ex_y):
    assert Position2D(x, y).move_right(mag) == Position2D(ex_x, ex_y)


def test_grid_bool():
    grid = Grid2DBool()
    pos = (5, 15)
    grid.turn_on(pos)
    assert grid.grid.get(pos)
    grid.turn_off(pos)
    assert not grid.grid.get(pos)
    grid.turn_off(pos)
    assert not grid.grid.get(pos)
    grid.toggle(pos)
    assert grid.grid.get(pos)
    grid.toggle(pos)
    assert not grid.grid.get(pos)


def test_grid_int():
    grid = Grid2Dint()
    pos = (5, 15)
    grid.turn_on(pos)
    assert grid.grid.get(pos) == 1
    grid.turn_off(pos)
    assert grid.grid.get(pos) == 0
    grid.turn_off(pos)
    assert grid.grid.get(pos) == 0
    grid.toggle(pos)
    assert grid.grid.get(pos) == 2
