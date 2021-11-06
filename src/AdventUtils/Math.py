from typing import Optional


def bitwise_not(operand: int, mask: Optional[int] = None) -> int:
    if mask:
        return ~operand & mask
    return ~operand


def bitwise_or(a: int, b: int, mask: Optional[int] = None) -> int:
    if mask:
        return (a | b) & mask
    return a | b


def bitwise_and(a: int, b: int, mask: Optional[int] = None) -> int:
    if mask:
        return (a & b) & mask
    return a & b


def bitwise_lshift(a: int, magnitude: int, mask: Optional[int] = None):
    if mask:
        return (a << magnitude) & mask
    return a << magnitude


def bitwise_rshift(a: int, magnitude: int, mask: Optional[int] = None):
    if mask:
        return (a >> magnitude) & mask
    return a >> magnitude
