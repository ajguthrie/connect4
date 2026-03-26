"""
Connect 4 game
"""

def border_line():
  print("+---" * 7 + "+")

def content_line_display(board_list):
  labels = [str(i) for i in range(1,8)]
  print("  " + "   ".join(labels))
  for sublist in board_list:
    border_line()
    row_string = ""
    blank_row = ""
    for item in sublist:
      row_string += f"| {item} "
      blank_row += "|   "
    row_string += "|"
    blank_row += "|"
    print(blank_row)
    print(row_string)
    print(blank_row)
  border_line()

def column_choice():
  done = False
  while not done:
    column = input("Which column would you like to put your piece? ")
    try:
      col_int = int(column)
      if 1 <= col_int <= 7:
        return col_int
      else: 
        print("Outside range 1-7! Please try again.")
    except ValueError:
      print("Invalid entry. Please try again.")

def drop_piece(board, column, symbol):
  column = column - 1
  for i in range(len(board)-1, -1, -1):
    if board[i][column] == ' ':
      board[i][column] = symbol
      return True
  return False

def check_vert(board, symbol):
  for r in range(3):
    for c in range(7):
      if (board[r][c] == symbol and board[r + 1][c] == symbol
          and board[r + 2][c] == symbol and board[r + 3][c] == symbol):
        return True
  return False

def check_horiz(board, symbol):
  for r in range(6):
    for c in range(4):
      if (board[r][c] == symbol and board[r][c + 1] == symbol 
          and board[r][c + 2] == symbol and board[r][c + 3] == symbol):
        return True
  return False

def check_diag(board, symbol):
  # down and right
  for r in range(3):
    for c in range(4):
      if (board[r][c] == symbol and board[r + 1][c + 1] == symbol and 
          board[r + 2][c + 2] == symbol and board[r + 3][c + 3] == symbol):
        return True
      
  # up and right
  for r in range(5, 2, -1):
    for c in range(4):
      if (board[r][c] == symbol and board[r - 1][c + 1] == symbol and 
          board[r - 2][c + 2] == symbol and board[r - 3][c + 3] == symbol):
        return True
  return False
      
def main():
  board = [[" "] * 7 for i in range(6)]
  current_player = "X"

  done = False
  while not done:
    content_line_display(board)
    print(f"It is {current_player}'s turn.")

    column = column_choice()
    if drop_piece(board, column, current_player):
      win_conditions = [
      check_vert(board, current_player), 
      check_horiz(board, current_player), 
      check_diag(board, current_player)
      ]

      if any(win_conditions):
        content_line_display(board)
        print(f"🎉 PLAYER {current_player} HAS WON THE GAME! 🎉")
        done = True
        break 

      if current_player == "X":
        current_player = "O"
      else:
        current_player = "X"
    else: 
      print("Column is full! Please pick another one.")

if __name__ == "__main__":
  main()