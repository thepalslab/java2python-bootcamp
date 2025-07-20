# src/py100days/days/__init__.py
# Explicit exports keep imports predictable.
__all__ = ["day01", "day02"]

from . import day01  # enables: from py100days.days import day01
from . import day02  # enables: from py100days.days import day02
