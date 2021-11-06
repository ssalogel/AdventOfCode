from AdventUtils.holders import Box


def test_box_get_smallest_size():
    assert Box(2, 3, 4).get_smallest_side_size() == 6
    assert Box(1, 1, 10).get_smallest_side_size() == 1


def test_box_get_total_surface():
    assert Box(2, 3, 4).get_total_surface() == 52
    assert Box(1, 1, 10).get_total_surface() == 42


def test_box_get_volume():
    assert Box(2, 3, 4).get_volume() == 24
    assert Box(1, 1, 10).get_volume() == 10


def test_box_get_smallest_perimeter():
    assert Box(2, 3, 4).get_smallest_perimeter() == 10
    assert Box(1, 1, 10).get_smallest_perimeter() == 4
