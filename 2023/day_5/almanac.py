
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


def in_range(source_value, source_start, range_len) -> bool:
    return source_value in range(source_start, source_start + range_len + 1)


def get_dest_value(source_value, map):
    dest_value = source_value
    for line in map:
        dest_start, source_start, range_len = line
        cond = in_range(source_value, source_start, range_len)
        if cond:

            offset = source_value - source_start
            dest_value = dest_start + offset
            # debug
            # if source_value == 14:
            #     ic(offset)
            #     ic(dest_value)
    return dest_value


# seed = seeds[0]
locations = []
for seed in seeds:
    soil = get_dest_value(seed, seed_to_soil_map)
    fertilizer = get_dest_value(soil, soil_to_fertilizer_map)
    water = get_dest_value(fertilizer, fertilizer_to_water_map)
    light = get_dest_value(water, water_to_light_map)
    temperature = get_dest_value(light, light_to_temperature_map)
    humidity = get_dest_value(temperature, temperature_to_humidity_map)
    location = get_dest_value(humidity, humidity_to_location_map)

    locations.append(location)

    if seed == 14:
        ic(seed)
        ic(soil)
        ic(fertilizer)
        ic(water)
        ic(light)
        ic(temperature)
        ic(humidity)
        ic(location)

    if seed == 79:
        assert location == 82
    # if seed == 14:
    #     assert location == 43
    if seed == 55:
        assert location == 86
    if seed == 13:
        assert location == 35


print(min(locations))

# debug: seed 14 -> location 43
'''
Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35
'''
