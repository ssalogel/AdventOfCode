from src.AdventUtils.Day import Day
from sys import maxsize
from functools import reduce


class Day16(Day):
    def __init__(self, content=None):
        super().__init__(day=16, year=2021, content=content)

    def parse_content(self, content: str):

        # dictionary here simplifies the previous line:
        # return ''.join(format(b, '04b') for b in b"".join([int(c, 16).to_bytes(1, byteorder='big') for c in content]))
        translate = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                     '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                     'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
        return ''.join([translate[b] for b in content])

    @staticmethod
    def get_type4(binary_data: str):
        end_block = 0
        while binary_data[end_block] != '0':
            end_block += 5
        end = end_block + 5
        num_w_pads = binary_data[:end]
        bin_num = [b for i, b in enumerate(num_w_pads) if i % 5 != 0]
        return int(''.join(bin_num), 2), end

    def extract_packet(self, packet: str, numbers=None):
        cummul_offset = 0
        res = []
        if numbers is None:
            numbers = maxsize
        while cummul_offset < len(packet)-10 and len(res) < numbers:
            ver = int(packet[cummul_offset:cummul_offset+3], 2)
            cummul_offset += 3
            type_elem = int(packet[cummul_offset:cummul_offset+3], 2)
            cummul_offset += 3
            if type_elem == 4:
                value, offset = self.get_type4(packet[cummul_offset:])
                res.append((ver, type_elem, value))
                cummul_offset += offset
            else:
                lenID = packet[cummul_offset]
                cummul_offset += 1
                if lenID == '0':
                    subpackets_len = int(packet[cummul_offset:cummul_offset+15], 2)
                    cummul_offset += 15
                    subpackets = packet[cummul_offset:cummul_offset+subpackets_len]
                    cummul_offset += subpackets_len
                    r, _ = self.extract_packet(subpackets)
                elif lenID == '1':
                    subpackets_num = int(packet[cummul_offset:cummul_offset+11], 2)
                    cummul_offset += 11
                    r, offset = self.extract_packet(packet[cummul_offset:], subpackets_num)
                    cummul_offset += offset
                res.append((ver, type_elem, r))
        return res, cummul_offset

    def sum_ver(self, tree) -> int:
        if tree[1] != 4:
            return tree[0] + sum(self.sum_ver(t) for t in tree[2])
        return tree[0]

    def solve_tree(self, tree) -> int:
        type_subtree = tree[1]
        subtree = tree[2]
        match type_subtree:
            case 4:
                return subtree
            case 0:
                return sum(self.solve_tree(t) for t in subtree)
            case 1:
                return reduce(lambda x, y: x * y, [self.solve_tree(t) for t in subtree], 1)
            case 2:
                return min(self.solve_tree(t) for t in subtree)
            case 3:
                return max(self.solve_tree(t) for t in subtree)
            case 5:
                return int(self.solve_tree(subtree[0]) > self.solve_tree(subtree[1]))
            case 6:
                return int(self.solve_tree(subtree[0]) < self.solve_tree(subtree[1]))
            case 7:
                return int(self.solve_tree(subtree[0]) == self.solve_tree(subtree[1]))

    def part1(self, parsed_content) -> int:
        res, _ = self.extract_packet(parsed_content)
        return self.sum_ver(res.pop())

    def part2(self, parsed_content) -> int:
        tree, _ = self.extract_packet(parsed_content)
        return self.solve_tree(tree.pop())
