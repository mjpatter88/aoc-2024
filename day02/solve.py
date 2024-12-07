
def solve():
  with open("input.txt") as in_file:
    reports = []
    for line in in_file.readlines():
      numbers = line.strip().split()
      reports.append([int(num) for num in numbers])

  num_safe = total_safe(reports)
  print(f"Part 1 solution: {num_safe}")

  num_safe_with_damp = total_safe_with_damp(reports)
  print(f"Part 2 solution: {num_safe_with_damp}")


def total_safe_with_damp(reports: list[list[int]]) -> int:
  return sum(is_safe_with_damp(report) for report in reports)

def total_safe(reports: list[list[int]]) -> int:
  return sum(is_safe(report) for report in reports)

def is_safe(report: list[int]) -> bool:
  assert(len(report) >= 2)

  is_increasing = True
  if report[1] < report[0]:
    is_increasing = False

  for index, val in enumerate(report):
    if index > 0:
      previous_val = report[index-1]
      if is_increasing and (previous_val >= val):
        return False
      if not is_increasing and (val >= previous_val):
        return False

      diff = abs(val - previous_val)
      if diff < 1 or diff > 3:
        return False

  # print(report)
  return True

def is_safe_with_damp(report: list[int]) -> bool:
  if is_safe(report):
    return True

  # try removing each number to see if it becomes safe
  # probably could be more efficient
  for x in range(len(report)):
    # use slicing to exclude a single number
    new_report = report[:x] + report[x+1:]
    if is_safe(new_report):
      return True

  return False

if __name__ == "__main__":
  solve()
