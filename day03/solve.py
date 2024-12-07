import re

def solve():
  with open("input.txt") as in_file:
    code = in_file.read().strip()

  muls = re.findall("mul\([0-9]+,[0-9]+\)", code)
  # print(muls)

  total = 0
  for mul in muls:
    # Capture the first and second numbers
    p = re.compile("mul\(([0-9]+),([0-9]+)\)")
    factors = p.match(mul)
    assert(factors)
    if factors:
      first, second = factors.groups()
      total += int(first) * int(second)

  print(f"Solution to part 1: {total}")




if __name__ == "__main__":
  solve()
