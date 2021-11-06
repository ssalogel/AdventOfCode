from AdventUtils.Grid2D import Position2D


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
