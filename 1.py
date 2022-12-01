from itertools import groupby
from pathlib import Path

lines = iter(Path("1.input").read_text().splitlines())

elves = []
for key, group in groupby(lines, key=bool):
    if not key:
        continue
    elves.append(sum(map(int, group)))

print(max(elves))
print(sum(sorted(elves)[-3:]))
