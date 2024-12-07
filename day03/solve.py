import re

def solve():
  with open("input.txt") as in_file:
    code = in_file.read().strip()

  muls = re.findall(r"mul\([0-9]+,[0-9]+\)", code)
  # print(muls)

  total = 0
  for mul in muls:
    # Capture the first and second numbers
    p = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    factors = p.match(mul)
    assert(factors)
    if factors:
      first, second = factors.groups()
      total += int(first) * int(second)

  print(f"Solution to part 1: {total}")

  second_total = 0

  dos_and_donts = [match for match in re.finditer(r"(don't|do)", code)]
  toggles = [(d.start(), d.groups()[0]) for d in dos_and_donts]
  # print(toggles)

  muls = [match for match in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", code)]
  for mul in muls:
    position = mul.start()
    first, second = mul.groups()
    # print(position)
    # print(f"{first},{second}")

    if is_active(toggles, position):
      second_total += int(first) * int(second)

  print(f"Solution to part 2: {second_total}")

def is_active(toggles: list[tuple[int, str]], position: int) -> bool:
  # Walk backwards through the list of toggles
  for toggle in reversed(toggles):
    if toggle[0] < position:
      if toggle[1] == "don't":
        return False
      else:
        return True

  # If no toggle applies, then it is active
  return True



if __name__ == "__main__":
  solve()
