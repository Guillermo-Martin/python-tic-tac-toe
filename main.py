tictactoe = {
  "row0": "   ",
  "col1": "1 ",
  "col2": "2 ",
  "col3": "3 ",
  "row1": "A",
  "a1": "X",
  "a2": "X",
  "a3": "X",
  "row2": "B",
  "b1": "X",
  "b2": "X",
  "b3": "X",
  "row3": "C",
  "c1": "X",
  "c2": "X",
  "c3": "X"
}


# ---------- creating the grid ----------
full_grid = ""

for key in tictactoe:
  # if you're at the end of a row in the game area add a line break after the X or O
  if key == "a3" or key == "b3":
    full_grid += f"{tictactoe[key]}\n  -----------\n"
  # if you're at the end of the row label for column number, add the number and add line breaks
  elif key == "col3":
    full_grid += f"{tictactoe[key]}\n\n"
  # else if you're at the very last row and column, or the column label row last column, just add the character
  elif key == "row0" or key == "c3":
    full_grid += f"{tictactoe[key]}"
  # add the row letters
  elif key == "row1" or key == "row2" or key == "row3" or key == "col1" or key == "col2":
    full_grid += f"{tictactoe[key]}  "
  # else, print the X or O and add a line divider
  else:
    full_grid += f"{tictactoe[key]} | "

# show tic tac toe board
print(f"""
{full_grid}\n
""")
