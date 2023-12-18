from __future__ import annotations

from typing import Optional

from src.AdventUtils.Day import Day


class File:
    def __init__(self, name: str, folder: bool, size: int = 0):
        self.name = name
        self.is_folder = folder
        self._size = size
        self.parent: Optional["File"] = None
        self.children: dict[str, "File"] = {} if self.is_folder else None

    def get_child(self, name: str) -> "File":
        return self.children[name]

    def add_child(self, child: "File"):
        child.parent = self
        self.children[child.name] = child

    @property
    def size(self):
        if self.is_folder and self._size == 0:
            self._size = sum(c.size for c in self.children.values())
        return self._size

    def __repr__(self):
        return f"dir={self.is_folder}, {self.name}: {self._size} [{self.children}]"


class Day7(Day):
    def __init__(self, content=None):
        super().__init__(day=7, year=2022, content=content)

    def parse_content(self, content: str):
        return content.splitlines()

    def build_file_tree(self, instrs: list[str]) -> File:
        root = File(name="/", folder=True)
        current = root
        for instr in instrs:
            if instr == "$ ls":
                pass
            elif instr.startswith("$ cd"):
                arg = instr[5:]
                if arg == "/":
                    current = root
                elif arg == "..":
                    current = current.parent
                else:
                    current = current.get_child(arg)
            else:
                ident, name = instr.split(" ")
                if ident.isnumeric():
                    f = File(name=name, folder=False, size=int(ident))
                else:
                    f = File(name=name, folder=True)
                current.add_child(f)
        return root

    def nb_folder_with_eqls_size(self, root: File, limit: int) -> int:
        if not root.is_folder:
            return 0
        return (root.size if root.size <= limit else 0) + sum(
            self.nb_folder_with_eqls_size(c, limit) for c in root.children.values()
        )

    def find_folder_to_free(self, root: File, target_size: int) -> File:
        if not any(
            [c.size >= target_size and c.is_folder for c in root.children.values()]
        ):
            return root
        potential = [
            self.find_folder_to_free(x, target_size)
            for x in filter(
                lambda x: x.size >= target_size and x.is_folder, root.children.values()
            )
        ]
        potential.sort(key=lambda x: x.size)
        return potential[0]

    def part1(self, parsed_content) -> int:
        files = self.build_file_tree(parsed_content)
        s = files.size
        return self.nb_folder_with_eqls_size(files, 100000)

    def part2(self, parsed_content) -> int:
        files = self.build_file_tree(parsed_content)
        total = 70000000
        goal = 30000000
        available = total - files.size
        to_free = goal - available
        f = self.find_folder_to_free(files, to_free)
        return f.size


if __name__ == "__main__":
    input_content = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
    d = Day7(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
