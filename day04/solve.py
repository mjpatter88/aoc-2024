
def solve():
  with open("input.txt") as in_file:
    raw_rows = in_file.readlines()
    rows = [row.strip() for row in raw_rows]

  total = 0
  for row_index in range(len(rows)):
    for col_index in range(len(rows[row_index])):
      total += words_from_start(rows, row_index, col_index)

  print(f"Solution to part 1: {total}")

def words_from_start(rows: list[str], row_index: int, col_index: int) -> int:
  total = 0
  funcs = [
    is_word_going_left, is_word_going_right, is_word_going_up,
    is_word_going_down, is_word_going_up_left, is_word_going_up_right,
    is_word_going_down_left, is_word_going_down_right
  ]
  for func in funcs:
    if func(rows, row_index, col_index):
      # print(f"{row_index}, {col_index}")
      total += 1
  return total

def is_word_going_left(rows: list[str], row_index: int, col_index: int) -> bool:
  row = rows[row_index]
  if col_index < 3:
    return False

  if row[col_index] == "X" and row[col_index-1] == "M" and row[col_index-2] =="A" and row[col_index-3] == "S":
    return True

  return False

def is_word_going_right(rows: list[str], row_index: int, col_index: int) -> bool:
  row = rows[row_index]
  if len(row) < col_index + 4:
    return False

  if row[col_index] == "X" and row[col_index+1] == "M" and row[col_index+2] =="A" and row[col_index+3] == "S":
    return True

  return False

def is_word_going_up(rows: list[str], row_index: int, col_index: int) -> bool:
  if row_index < 3:
    return False

  if rows[row_index][col_index] == "X" and rows[row_index-1][col_index] == "M" and rows[row_index-2][col_index] =="A" and rows[row_index-3][col_index] == "S":
    return True

  return False

def is_word_going_down(rows: list[str], row_index: int, col_index: int) -> bool:
  if len(rows) < row_index + 4:
    return False

  if rows[row_index][col_index] == "X" and rows[row_index+1][col_index] == "M" and rows[row_index+2][col_index] =="A" and rows[row_index+3][col_index] == "S":
    return True

  return False

def is_word_going_up_left(rows: list[str], row_index: int, col_index: int) -> bool:
  if row_index < 3 or col_index < 3:
    return False

  if rows[row_index][col_index] == "X" and rows[row_index-1][col_index-1] == "M" and rows[row_index-2][col_index-2] =="A" and rows[row_index-3][col_index-3] == "S":
    return True

  return False

def is_word_going_up_right(rows: list[str], row_index: int, col_index: int) -> bool:
  row = rows[row_index]
  if len(row) < col_index + 4 or row_index < 3:
    return False

  if rows[row_index][col_index] == "X" and rows[row_index-1][col_index+1] == "M" and rows[row_index-2][col_index+2] =="A" and rows[row_index-3][col_index+3] == "S":
    return True

  return False

def is_word_going_down_left(rows: list[str], row_index: int, col_index: int) -> bool:
  if len(rows) < row_index + 4 or col_index < 3:
    return False

  if rows[row_index][col_index] == "X" and rows[row_index+1][col_index-1] == "M" and rows[row_index+2][col_index-2] =="A" and rows[row_index+3][col_index-3] == "S":
    return True

  return False

def is_word_going_down_right(rows: list[str], row_index: int, col_index: int) -> bool:
  row = rows[row_index]
  if len(row) < col_index + 4 or len(rows) < row_index + 4:
    return False

  if rows[row_index][col_index] == "X" and rows[row_index+1][col_index+1] == "M" and rows[row_index+2][col_index+2] =="A" and rows[row_index+3][col_index+3] == "S":
    return True

  return False

if __name__ == "__main__":
  solve()
