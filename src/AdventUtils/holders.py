class Box:
    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height
        self.top = length * width
        self.front = width * height
        self.side = height * length

    def get_smallest_side_size(self) -> int:
        return min(self.top, self.front, self.side)

    def get_total_surface(self) -> int:
        return (2 * self.side) + (2 * self.front) + (2 * self.top)

    def get_volume(self) -> int:
        return self.length * self.width * self.height

    def get_smallest_perimeter(self) -> int:
        return (
            self.length
            + self.width
            + self.height
            - max(self.length, self.width, self.height)
        ) * 2
