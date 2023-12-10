
# from pprint import pprint as pp
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]

datafile = datafiles[1]

with open(datafile, "r") as rf:
    lines = rf.read().split('\n\n')

# lines = [line.removesuffix("\n") for line in lines]
# blocks = [block.strip() for block in lines.split('\n\n')]

# for line in lines:
#     print(line)

# print(lines[2])

seeds = [int(i) for i in lines[0].split(":")[1].strip().split()]


def get_map(j: int) -> list[list[int]]:
    return [
    [int(value) for value in i.split(' ')]
    for i in lines[j].split("\n")[1:]
    ]


seed_to_soil_map = get_map(1)
soil_to_fertilizer_map = get_map(2)
fertilizer_to_water_map = get_map(3)
water_to_light_map = get_map(4)
light_to_temperature_map = get_map(5)
temperature_to_humidity_map = get_map(6)
humidity_to_location_map = get_map(7)

# each line:
# destination range start, source range start, and the range length.

# ic(seeds)
# ic(seed_to_soil_map)

# 1. convert seed value to location
# 1a. convert seed value to soil value
# 1b. convert soil value to fertilizer value
# 1_. ...
# 2. repeat for all seeds
# 3. find the minimum location value

seed = seeds[0]
ic(seed)


def in_range(source_start, range_len) -> bool:
    return seed in range(source_start, source_start + range_len + 1)


def get_dest_value(source_value, map):
    dest_value = source_value
    for line in map:
        dest_start, source_start, range_len = line
        cond = in_range(source_start, range_len)
        if cond:
            offset = source_value - source_start
            dest_value = dest_start + offset
    return dest_value


soil = get_dest_value(seed, seed_to_soil_map)
fertilizer = get_dest_value(soil, soil_to_fertilizer_map)
water = get_dest_value(fertilizer, fertilizer_to_water_map)
light = get_dest_value(water, water_to_light_map)
temperature = get_dest_value(light, light_to_temperature_map)
humidity = get_dest_value(temperature, temperature_to_humidity_map)
location = get_dest_value(humidity, humidity_to_location_map)

ic(soil)
ic(fertilizer)
ic(water)
ic(light)
ic(temperature)  # correct temperature: 78
ic(humidity)
ic(location)