from string import ascii_lowercase
from hashlib import md5


def rot13(string: str, magnitude: int = 13):
    return "".join(
        [
            ascii_lowercase[(ascii_lowercase.find(c) + magnitude) % 26]
            for c in string.lower()
            if c in ascii_lowercase
        ]
    )


def find_hash(start: str, pattern: str, number: int = 1) -> list[tuple[int, str]]:
    x = 0
    res = []
    while True:
        hash = md5((start + str(x)).encode()).hexdigest()
        if hash.startswith(pattern):
            res.append((x, hash))
            if len(res) == number:
                return res
        x += 1
