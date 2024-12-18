
from dataclasses import dataclass
from itertools import filterfalse, islice
import math
# from pprint import pprint as pp
from tqdm import tqdm
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_full_path import get_full_path  # type: ignore


def get_raw_monkeys():

    raw_monkeys = []
    datafiles = [
        "sample.txt",
        "input.txt",
        ]
    datafile = get_full_path("2022", "day_11", datafiles[1])

    with open(datafile, "r") as rf:
        while True:
            filt_rf = filterfalse(lambda line: line.startswith("\n"), rf)
            monkey = list(islice(filt_rf, 6))
            monkey = [line.strip().strip("\n").rstrip(":") for line in monkey]
            if not monkey:
                break
            raw_monkeys.append(monkey)
    return raw_monkeys


raw_monkeys = get_raw_monkeys()
clean_monkeys = []

for monkey in raw_monkeys:
    monkey_id = int(monkey[0].split()[-1])
    starting_items = [int(x) for x in monkey[1].split(":")[-1].strip().split(", ")]
    operation = monkey[2].split(":")[-1].strip().replace("new = ", "")
    test_divisible_by = int(monkey[3].split(":")[-1].strip().split()[-1])
    next_monkey_on_true = int(monkey[4].split(":")[-1].strip().split()[-1])
    next_monkey_on_false = int(monkey[5].split(":")[-1].strip().split()[-1])

    clean_monkey = {
        "id": monkey_id,
        "starting_items": starting_items,
        "operation": operation,
        "test_divisible_by": test_divisible_by,
        "next_monkey_on_true": next_monkey_on_true,
        "next_monkey_on_false": next_monkey_on_false,
    }
    clean_monkeys.append(clean_monkey)


# TODO; use algo-lib
# def is_prime(n: int) -> bool:
#     for k in range(2, int(math.sqrt(n)) + 1):
#         if n % k == 0:
#             return False
#     return True


tests = []
for monkey in clean_monkeys:
    assert is_prime(monkey["test_divisible_by"]) is True
    tests.append(monkey["test_divisible_by"])


least_common_multiple = math.lcm(*tests)


@dataclass
class Monkey:
    id: int
    starting_items: list
    test_divisible_by: int
    operation: str
    next_monkey_on_true: int
    next_monkey_on_false: int

    def update_worry_level(self, old):
        res = eval(self.operation)

        # part 1
        # res //= 3

        # part 2
        res %= least_common_multiple

        return res

    def get_next_monkey(self, new) -> int:
        if new % self.test_divisible_by == 0:
            return self.next_monkey_on_true
        return self.next_monkey_on_false


monkeys = [Monkey(**clean_monkey) for clean_monkey in clean_monkeys]

inspections = {"round": 0, "monkeys": {idx: 0 for idx, _ in enumerate(monkeys)}}
rounds = 10_000  # 20

for i in tqdm(range(rounds)):
    inspections["round"] += 1
    for monkey in monkeys:
        if len(monkey.starting_items) == 0:
            continue
        inspections["monkeys"][monkey.id] += len(monkey.starting_items)
        for starting_item in monkey.starting_items:
            updated_worry_level = monkey.update_worry_level(starting_item)
            next_monkey = monkey.get_next_monkey(updated_worry_level)
            for ape in monkeys:
                if ape.id == next_monkey:
                    ape.starting_items.append(updated_worry_level)
        monkey.starting_items = []

# pp(monkeys)
monkey_activity = sorted(
    inspections["monkeys"].items(), key=lambda x: x[1], reverse=True
)[:2]

monkey_business = monkey_activity[0][1] * monkey_activity[1][1]

print(inspections["monkeys"])
print(monkey_activity)
print(f"{monkey_business = }")
