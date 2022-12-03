import sys
from string import ascii_lowercase, ascii_uppercase

PRIORITIES = dict(zip(ascii_lowercase + ascii_uppercase, range(1, 53)))

data = sys.stdin.read().splitlines()
sum = 0
for rucksack in data:
    half = len(rucksack) // 2
    compartment1, compartment2 = rucksack[:half], rucksack[half:]
    assert len(compartment1) == len(compartment2), "compartments of the rucksack have the same length"
    common = set(compartment1) & set(compartment2)
    assert len(common) == 1, "exactly one item is common to both compartments"
    sum += PRIORITIES[common.pop()]
print(sum)

lines = iter(data)
sum = 0
for r1, r2, r3 in zip(lines, lines, lines):
    common = set(r1) & set(r2) & set(r3)
    assert len(common) == 1, "exactly one item is common to each group"
    sum += PRIORITIES[common.pop()]
print(sum)
