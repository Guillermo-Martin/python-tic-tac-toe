tictactoe = {
  "row0": " ",
  "col1": "1",
  "col2": "2",
  "col3": "3",
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

# variables
game_over = False

# ---------- function to create the grid ----------
def create_grid(dict):
  # define the final grid
  final_grid = ""

  for key in tictactoe:
    # build the first row (for labeling columns)
    if key == "row0":
      final_grid += f"{tictactoe[key]}  "
    # if you're at the end of the first row, add line breaks with no lines
    elif key == "col3":
      final_grid += f"{tictactoe[key]}\n\n"
    # if you're at the end of the A and B rows, ad a line break with a line
    elif key == "a3" or key == "b3":
      final_grid += f"{tictactoe[key]}\n  -----------\n"
    # if you're at the start of the A, B, and C rows, add spaces (this is the letter column)
    elif key == "row1" or key == "row2" or key == "row3":
      final_grid += f"{tictactoe[key]}  "
    # if you're in the "1" or "2" columns, add spaces to align with the grid
    elif key == "col1" or key == "col2":
      final_grid += f"{tictactoe[key]}   "
    # if you're in the last row (C), add line breaks to make it easier to read
    elif key == "c3":
      final_grid += f"{tictactoe[key]}\n\n"
    # otherwise, add the letter, a divider, and appropriate spacing
    else:
      final_grid += f"{tictactoe[key]} | "

  # return the final grid
  return final_grid


# at start of the game, show the empty grid
starting_grid = create_grid(tictactoe)
print(f"""\n{starting_grid}""")

# starting the game
while game_over is False:
  player = input("What is your letter? ")
  tictactoe["a1"] = player
  print(player)

  # ---------- show the filled out grid ----------
  full_grid = create_grid(tictactoe)

  # show tic tac toe board
  print(f"""\n{full_grid}""")
