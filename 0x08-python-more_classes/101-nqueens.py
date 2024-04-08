import sys

def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe (doesn't attack other queens).
  """
  # Check row and diagonals
  for i in range(col):
    if board[row][i] == 1:
      return False
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  for i, j in zip(range(row + 1, len(board)), range(col + 1, len(board))):
    if board[i][j] == 1:
      return False
  return True

def solve_n_queens(board, col):
  """
  Solves the N queens problem recursively using backtracking.
  """
  if col >= len(board):
    # All queens placed, print the solution
    solution = [row for row, col in enumerate(board) if col]
    print(solution)
    return

  for i in range(len(board)):
    if is_safe(board, i, col):
      board[i][col] = 1
      solve_n_queens(board, col + 1)
      board[i][col] = 0  # Backtrack

def main():
  """
  Main function for handling user input and solving N queens problem.
  """
  if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

  if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)

  board = [[0 for _ in range(n)] for _ in range(n)]
  solve_n_queens(board, 0)

if __name__ == "__main__":
  main()

