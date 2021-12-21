from src.AdventUtils.Day import Day


class Day7(Day):
    def __init__(self, content=None):
        super().__init__(day=7, year=2016, content=content)

    def parse_content(self, content: str) -> list[tuple[list[str], list[str]]]:
        adresses = content.strip().replace(']', '[').split('\n')
        inter_ip_hyper = [ad.split('[') for ad in adresses]
        return [(ad[0::2], ad[1::2]) for ad in inter_ip_hyper]

    def has_abba(self, string: str) -> bool:
        for a, b, c, d in zip(string, string[1:], string[2:], string[3:]):
            if a == d and b == c and a != b:
                return True
        return False

    def get_aba(self, strings: list[str]) -> set[str]:
        abas: set[str] = set()
        for string in strings:
            for a, b, c in zip(string, string[1:], string[2:]):
                if a == c and a != b:
                    abas.add(''.join([a, b, c]))
        return abas

    def check_bab(self, strings: list[str], aba: set[str]):
        pot_bab = [''.join([c[1], c[0], c[1]]) for c in aba]
        for string in strings:
            for pot_b in pot_bab:
                if pot_b in string:
                    return True
        return False

    def is_valid_ip(self, ip: tuple[list[str], list[str]]) -> bool:
        return any(map(self.has_abba, ip[0])) and not any(map(self.has_abba, ip[1]))

    def part1(self, parsed_content: list[tuple[list[str], list[str]]]) -> int:
        return sum(map(self.is_valid_ip, parsed_content))

    def part2(self, parsed_content: list[tuple[list[str], list[str]]]) -> int:
        return sum(self.check_bab(hyper, self.get_aba(super)) for super, hyper in parsed_content)
