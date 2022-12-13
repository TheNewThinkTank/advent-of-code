from dataclasses import dataclass
from itertools import filterfalse, islice
from pprint import pprint as pp


@dataclass
class Monkey:
    id: int
    starting_items: list
    test_divisible_by: int
    operation: str
    next_monkey_on_true: int
    next_monkey_on_false: int

    def update_worry_level(self):
        old = self.starting_items[0]
        res = eval(self.operation)
        self.starting_items[0] = res
        return res

    def test(self) -> bool:
        return self.starting_items[0] % self.test_divisible_by == 0

    def remove_item(self):
        del self.starting_items[0]

    def receive_item(self, item):
        self.starting_items.append(item)


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

first_monkey = monkeys[0]

for starting_item in first_monkey.starting_items:
    print(starting_item)

    updated_worry_level = first_monkey.update_worry_level()

    print(starting_item, updated_worry_level)

    # first_monkey.test()

    # next monkey receives
