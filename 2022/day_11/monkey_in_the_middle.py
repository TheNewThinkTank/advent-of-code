from dataclasses import dataclass
from itertools import filterfalse, islice
from pprint import pprint as pp


@dataclass
class Monkey:
    id: int
    starting_items: list
    num: int
    worry_level: int
    operation: str

    def update_worry_level(self):
        return eval(self.operation)

    def test(self) -> bool:
        return self.worry_level % self.num == 0


# worry_level: int


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
# pp(raw_monkeys)

monkeys = []
for monkey in raw_monkeys:

    monkey_id = int(monkey[0].split()[-1])
    starting_items = [int(x) for x in monkey[1].split(":")[-1].strip().split(", ")]
    operation = monkey[2].split(":")[-1].strip()
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
    monkeys.append(clean_monkey)

pp(monkeys)
