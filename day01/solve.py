from collections import defaultdict

def run():
  l1 = []
  l2 = []
  with open("input.txt") as in_file:
    for line in in_file.readlines():
      first, _, _, second = line.strip().split(" ")
      l1.append(int(first))
      l2.append(int(second))

  assert(len(l1) == len(l2))
  # print(l1)
  # print(l2)

  difference = find_difference(l1, l2)
  print(f"Part 1 solution: {difference}")

  similarity_score = find_similarity_score(l1, l2)
  print(f"Part 2 solution: {similarity_score}")

def find_difference(l1: list[int], l2: list[int]) -> int:
  l1.sort()
  l2.sort()

  difference = 0
  for index, val in enumerate(l1):
    val2 = l2[index]
    difference += abs(val - val2)

  return difference

def find_similarity_score(l1: list[int], l2: list[int]) -> int:

  occurrences = defaultdict(int)
  for val in l2:
    occurrences[val] += 1

  score = 0
  for  val in l1:
    score += val * occurrences[val]

  return score

if __name__ == "__main__":
  run()
