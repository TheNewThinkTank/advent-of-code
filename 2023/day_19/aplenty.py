from pprint import pprint as pp
from collections import OrderedDict
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]
datafile = datafiles[1]


def get_data():
    with open(datafile, "r") as f:
        data = f.read()
    return data.split("\n\n")  # name, list[rules]


def get_wf_name_and_rules(workflow):
    wf_name = workflow.split("{")[0]
    wf_rules = workflow.split("{")[1].strip("}").split(",")
    return wf_name, wf_rules


def get_wf_dict(wf_rules):
    wf_dict = OrderedDict()
    for rule in wf_rules:
        if ':' in rule:
            wf_dict[rule.split(':')[1]] = rule.split(':')[0]
        else:
            wf_dict[rule] = ''
    return wf_dict


def get_all_parts(part_ratings):
    all_parts = []
    for part_rating in part_ratings:
        part_rating = part_rating.strip("{}")
        parts = part_rating.split(",")
        all_parts.append(
            {part.split("=")[0]: int(part.split("=")[1]) for part in parts}
        )
    return all_parts


def get_wfs(workflows):
    wfs = {}
    for workflow in workflows:
        wf_name, wf_rules = get_wf_name_and_rules(workflow)
        wf_dict = get_wf_dict(wf_rules)
        wfs[wf_name] = wf_dict
    return wfs


data = get_data()
workflows = data[0].split("\n")
part_ratings = data[1].split("\n")
all_parts = get_all_parts(part_ratings)
# pp(all_parts)

# pp(workflows)
# pp(part_ratings)
# workflow = workflows[0]
part_rating = all_parts[0]
# ic(part_rating)
wfs = get_wfs(workflows)
# pp(wfs)
# print(wfs['in'])

for name, cond in wfs['in'].items():

    if not cond:
        if name == "A" or name == "R":
            print("final status: ", name)
            break
        print("Start wf: ", name)
        break

    ic(name)
    # ic(cond)

    cond_parts = cond.partition(">") if ">" in cond else cond.partition("<")
    ic(cond_parts)

    category = cond_parts[0]
    operator = cond_parts[1]
    value = int(cond_parts[2])

    expression = f"{part_rating[category]} {operator} {value}"
    res = eval(expression)
    # ic(part_rating[category])
    ic(expression)
    ic(res)
