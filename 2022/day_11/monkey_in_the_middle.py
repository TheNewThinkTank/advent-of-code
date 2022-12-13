from dataclasses import dataclass
from itertools import filterfalse, islice
import math
from pprint import pprint as pp


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
        res = math.floor(res / 3)
        # self.starting_items[0] = res
        return res

    def get_next_monkey(self, new) -> int:
        if new % self.test_divisible_by == 0:
            return self.next_monkey_on_true - 1
        return self.next_monkey_on_false - 1

    # def remove_item(self):
    #     del self.starting_items[0]

    # def receive_item(self, item):
    #     self.starting_items.append(item)


def get_raw_monkeys():
    raw_monkeys = []
    with open("sample.txt", "r") as rf:
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

# pp(clean_monkeys)
monkeys = [Monkey(**clean_monkey) for clean_monkey in clean_monkeys]
# pp(monkeys)

# first_monkey = monkeys[0]
# third_monkey = monkeys[2]
# print(first_monkey)
# print(third_monkey)

# assert len(first_monkey.starting_items) > 0

for monkey in monkeys:
    if len(monkey.starting_items) == 0:
        continue
    for starting_item in monkey.starting_items:
        # print(starting_item)
        updated_worry_level = monkey.update_worry_level(starting_item)
        # print(starting_item, updated_worry_level)
        next_monkey = monkey.get_next_monkey(updated_worry_level)
        # print(next_monkey)

        for ape in monkeys:
            if ape.id == next_monkey:
                ape.starting_items.append(updated_worry_level)

    monkey.starting_items = []

pp(monkeys)
