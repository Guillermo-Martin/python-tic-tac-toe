tictactoe = {
  "row0": " ",
  "col1": "1 ",
  "col2": "2 ",
  "col3": "3 ",
  "row1": "A",
  "a1": " ",
  "a2": " ",
  "a3": " ",
  "row2": "B",
  "b1": " ",
  "b2": " ",
  "b3": " ",
  "row3": "C",
  "c1": " ",
  "c2": " ",
  "c3": " "
}

game_over = False


while game_over is False:
  full_grid = ""

  player = input("What is your letter? ")
  tictactoe["a1"] = player
  print(player)

  # ---------- creating the grid ----------
  for key in tictactoe:
    # if you're at the end of a row in the game area add a line break after the X or O
    if key == "a3" or key == "b3":
      full_grid += f"{tictactoe[key]}\n  -----------\n"
    # if you're at the end of the row label for column number, add the number and add line breaks
    elif key == "col3":
      full_grid += f"{tictactoe[key]}\n\n"
    elif key == "row0":
      full_grid += f"{tictactoe[key]}"
    # else if you're at the very last row and column, or the column label row last column, just add the character
    elif key == "c3":
      full_grid += f"{tictactoe[key]}\n\n\n"
    # add the row letters
    elif key == "row1" or key == "row2" or key == "row3" or key == "col1" or key == "col2":
      full_grid += f"{tictactoe[key]}  "
    # else, print the X or O and add a line divider
    else:
      full_grid += f"{tictactoe[key]} | "

  # show tic tac toe board
  print(f"""
  {full_grid}
  """)
