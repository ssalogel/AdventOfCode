from AdventUtils.Conway import FullBoardConway2D
import pytest


def create_game():
    game = FullBoardConway2D(to_on=lambda x: x == 3, to_off=lambda x: x < 2 or x > 3)
    on_pos = {(1, 0), (3, 0), (5, 0),
              (3, 1), (4, 1),
              (0, 2), (5, 2),
              (2, 3),
              (0, 4), (2, 4), (5, 4),
              (0, 5), (1, 5), (2, 5), (3, 5)}
    game.new_board(positions=on_pos, height=6, width=6)
    return game


def steps(game: FullBoardConway2D, amount: int, stuck_on: set[tuple[int, int]] = set) -> FullBoardConway2D:
    game.turn_on(stuck_on)
    for _ in range(amount):
        game.step()
        game.turn_on(stuck_on)
    return game


@pytest.mark.parametrize("nb_turn, stuck_on, nb_on", [
    (0, set(), 15),
    (1, set(), 11),
    (2, set(), 8),
    (3, set(), 4),
    (4, set(), 4),
    (0, {(0, 0), (0, 5), (5, 0), (5, 5)}, 17),
    (1, {(0, 0), (0, 5), (5, 0), (5, 5)}, 18),
    (2, {(0, 0), (0, 5), (5, 0), (5, 5)}, 18),
    (3, {(0, 0), (0, 5), (5, 0), (5, 5)}, 18),
    (4, {(0, 0), (0, 5), (5, 0), (5, 5)}, 14),
    (5, {(0, 0), (0, 5), (5, 0), (5, 5)}, 17)
])
def test_conway(nb_turn, stuck_on, nb_on):
    assert len(steps(create_game(), nb_turn, stuck_on).board) == nb_on
