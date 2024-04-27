import re
import sys
from importlib import import_module
from math import ceil
from os import path, listdir
from timeit import timeit
from typing import List


def get_all_problems() -> List[str]:
    pattern = re.compile(r"(\d+)\.py")

    problems = (match[1] for filename in listdir(path.dirname(path.realpath(__file__)))
                if (match := pattern.match(filename)))

    return sorted(problems, key=int)


def format_time(time: float) -> str:
    return f"{ceil(time * 1000)}ms" if time < 1 else f"{ceil(time)}s"


problems = get_all_problems() if len(sys.argv) == 1 else sys.argv[1:]

for problem in problems:
    if not problem.isnumeric():
        continue

    print(f"Problem {problem}:")
    time = format_time(timeit(lambda: import_module(f"euler.{problem}")))
    print(f"Execution completed in {time}")
    print()
