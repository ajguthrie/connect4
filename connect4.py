board_list = [[" "] * 7 for i in range(6)]

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
    

content_line_display(board_list)