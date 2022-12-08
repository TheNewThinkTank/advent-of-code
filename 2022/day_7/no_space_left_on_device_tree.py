import re

from treelib import Tree

datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[0]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]

cd_dir_regex = re.compile(r"^\$\scd\s(.*)")
dir_regex = re.compile(r"^dir\s(.*)")
file_regex = re.compile(r"^(\d*)\s(.*)")


class File:
    def __init__(self, size):
        self.size = size


def get_tree():
    dir_names = set()
    tree = Tree()
    tree.create_node("/", "/", data=File(0))  # root tree node
    current_dir = "/"

    for line in lines:
        is_changing_dir = re.search(cd_dir_regex, line)
        dir_content = re.search(dir_regex, line)
        file_content = re.search(file_regex, line)

        if is_changing_dir:
            current_dir = is_changing_dir.group(1)
        if current_dir == "..":
            continue

        if dir_content:
            dir_name = dir_content.group(1)
            while dir_name in dir_names:
                dir_name += "_$"
            dir_names.add(dir_name)

            tree.create_node(
                dir_name,
                dir_name,
                parent=current_dir,
                data=File(0),
            )

        if file_content:
            orig_file_size = tree.get_node(current_dir).data.size
            extra_file_size = int(file_content.group(1))
            file_size = orig_file_size + extra_file_size
            # node = tree.get_node(current_dir)
            # print(node.tag, node.data.size, file_size)
            tree.update_node(current_dir, data=File(file_size))

    return tree


tree = get_tree()
tree.show()


def update_tree():
    for node in tree.all_nodes()[::-1]:
        if node.is_leaf():
            continue
        for child in tree.children(node.tag):
            data = File(node.data.size + child.data.size)
            tree.update_node(node.tag, data=data)


update_tree()
tree.show(data_property="size")


def sum_small_nodes():
    small_nodes = []
    for node in tree.all_nodes():
        if node.data.size <= 100_000:
            small_nodes.append(node.data.size)
    return sum(small_nodes)


# small_nodes_sum = sum_small_nodes()
# print(small_nodes_sum)
