from AdventUtils.Grid2D import Position2D, Grid2DBool, Grid2Dint


def test_move_up():
    assert Position2D(0, 0).move_up() == Position2D(0, 1)
    assert Position2D(-1, -1).move_up() == Position2D(-1, 0)


def test_move_down():
    assert Position2D(0, 0).move_down() == Position2D(0, -1)
    assert Position2D(-1, -1).move_down() == Position2D(-1, -2)


def test_move_left():
    assert Position2D(0, 0).move_left() == Position2D(-1, 0)
    assert Position2D(-1, -1).move_left() == Position2D(-2, -1)


def test_move_right():
    assert Position2D(0, 0).move_right() == Position2D(1, 0)
    assert Position2D(-1, -1).move_right() == Position2D(0, -1)


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
