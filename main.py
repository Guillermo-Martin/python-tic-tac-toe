tictactoe = {
  "a1": "X",
  "a2": "X",
  "a3": "X",
  "b1": "X",
  "b2": "X",
  "b3": "X",
  "c1": "X",
  "c2": "X",
  "c3": "X"
}


# ---------- creating the grid ----------
full_grid = ""

for key in tictactoe:
  # if you're at the end of the row add a line break after the X or O
  if key == "a3" or key == "b3":
    full_grid += f"{tictactoe[key]}\n---------\n"
  # else if you're at the very last row and column, just add the X or O
  elif key == "c3":
    full_grid += f"{tictactoe[key]}"
  # else, print the X or O and add a line divider
  else:
    full_grid += f"{tictactoe[key]} | "

# show tic tac toe board
print(full_grid)
