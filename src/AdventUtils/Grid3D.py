from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Position3D:
    x: int = 0
    y: int = 0
    z: int = 0

    def get_connections(self):
        for delta_x, delta_y, delta_z in [
            (0, 0, 1),
            (0, 0, -1),
            (0, 1, 0),
            (0, -1, 0),
            (1, 0, 0),
            (-1, 0, 0),
        ]:
            yield Position3D(self.x + delta_x, self.y + delta_y, self.z + delta_z)
