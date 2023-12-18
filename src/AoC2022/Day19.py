from src.AdventUtils.Day import Day
import re
from dataclasses import dataclass
from collections import deque


@dataclass(frozen=True)
class Blueprint:
    name: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost_ore: int
    obsidian_robot_cost_clay: int
    geode_robot_cost_ore: int
    geode_robot_cost_obsidian: int

    def get_max_ore_cost(self):
        return max([self.geode_robot_cost_ore, self.ore_robot_cost, self.obsidian_robot_cost_ore, self.clay_robot_cost])


@dataclass(frozen=True)
class PondState:
    blueprint: Blueprint
    time: int = 0
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0
    ore_robot: int = 1
    clay_robot: int = 0
    obsidian_robot: int = 0
    geode_robot: int = 0

    def empty_step(self, magnitude):
        return PondState(
                blueprint=self.blueprint,
                time=self.time + magnitude,
                ore=self.ore + (self.ore_robot * magnitude),
                clay=self.clay + (self.clay_robot * magnitude),
                obsidian=self.obsidian + (self.obsidian_robot * magnitude),
                geode=self.geode + (self.geode_robot * magnitude),
                geode_robot=self.geode_robot,
                obsidian_robot=self.obsidian_robot,
                clay_robot=self.clay_robot,
                ore_robot=self.ore_robot
            )

    def build_robot(self, robot: str):
        return PondState(blueprint=self.blueprint,
                         time=self.time + 1,
                         ore=self.ore + self.ore_robot,
                         clay=self.clay + self.clay_robot,
                         obsidian=self.obsidian_robot + self.obsidian_robot,
                         geode=self.geode + self.geode_robot,
                         ore_robot=self.ore_robot + int(robot == "ore"),
                         clay_robot=self.clay_robot + int(robot == "clay"),
                         obsidian_robot=self.obsidian_robot + int(robot == "obsidian"),
                         geode_robot=self.geode_robot + int(robot == "geode")
                         )


def get_min_waiting_time(state: PondState) -> int:
    ore_time = min(state.blueprint.ore_robot_cost, state.blueprint.clay_robot_cost, state.blueprint.obsidian_robot_cost_ore, state.blueprint.geode_robot_cost_ore) - state.ore
    clay_time = state.blueprint.obsidian_robot_cost_clay - state.clay
    obsd_time = state.blueprint.geode_robot_cost_obsidian - state.obsidian
    return max(min(ore_time, clay_time, obsd_time), 1)


def get_best_state(blueprint: Blueprint, timelimit: int = 24) -> PondState:
    start = PondState(blueprint)
    queue: deque[PondState] = deque()
    queue.append(start)
    visited = set()
    best_state = start
    while len(queue) > 0:
        curr = queue.popleft()
        if curr.time >= timelimit:
            if curr.geode > best_state.geode:
                best_state = curr
            continue
        if curr in visited:
            continue
        visited.add(curr)
        if curr.blueprint.geode_robot_cost_ore <= curr.ore and curr.blueprint.geode_robot_cost_obsidian <= curr.obsidian:
            queue.append(curr.build_robot("geode"))
        if curr.obsidian_robot < curr.blueprint.geode_robot_cost_obsidian:
            if curr.blueprint.obsidian_robot_cost_ore <= curr.ore and curr.blueprint.obsidian_robot_cost_clay <= curr.clay:
                queue.append(curr.build_robot("obsidian"))
        if curr.clay_robot < curr.blueprint.obsidian_robot_cost_clay:
            if curr.blueprint.clay_robot_cost <= curr.ore:
                queue.append(curr.build_robot("clay"))
        if curr.ore_robot < curr.blueprint.get_max_ore_cost():
            if curr.blueprint.ore_robot_cost <= curr.ore:
                queue.append(curr.build_robot("ore"))
        min_time = get_min_waiting_time(curr)
        queue.append(curr.empty_step(min_time))
    return best_state


class Day19(Day):
    def __init__(self, content=None):
        super().__init__(day=19, year=2022, content=content)

    def parse_content(self, content: str):
        res = []
        for line in content.strip().splitlines():
            (
                nb,
                ore_rb_ore,
                clay_rb_ore,
                obs_rb_ore,
                obs_rb_clay,
                geo_rb_ore,
                geo_rb_obs,
            ) = tuple(
                map(
                    int,
                    re.match(
                        r"[A-Za-z \.]+(\d+):[A-Za-z \.]+(\d+)[A-Za-z \.]+(\d+)[A-Za-z \.]+(\d+)[A-Za-z \.]+(\d+)[A-Za-z \.]+(\d+)[A-Za-z \.]+(\d+)",
                        line,
                    ).groups(),
                )
            )
            res.append(Blueprint(
                nb,
                ore_rb_ore,
                clay_rb_ore,
                obs_rb_ore,
                obs_rb_clay,
                geo_rb_ore,
                geo_rb_obs,
            ))
        return res

    def part1(self, parsed_content) -> int:
        acc = 0
        return
        for blueprint in parsed_content:
            state = get_best_state(blueprint)
            acc += state.geode * state.blueprint.name
        return acc

    def part2(self, parsed_content) -> int:
        pass


if __name__ == "__main__":
    input_content = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian. 
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""
    d = Day19(content=input_content)
    print(d.part1(parsed_content=d.parse_content(content=d.content)))
    print(d.part2(parsed_content=d.parse_content(content=d.content)))
