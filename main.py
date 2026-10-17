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
x_player = True

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
  # get current player
  print("x player", x_player)

  # ask player which position they want to put their X or O in
  player_input = input(f"{'Player 1 (X),' if x_player else 'Player 2 (O),'} where would you like to go?: ").lower()

  # check input
  grid_options = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]


  if player_input in grid_options and tictactoe[player_input] == " ":
    # put player selection
    if x_player:
      tictactoe[player_input] = "X"
    else:
      tictactoe[player_input] = "O"

    # then change to other player
    x_player = not x_player
  else:
    print("Enter a valid location.")


  # ---------- show the filled out grid ----------
  full_grid = create_grid(tictactoe)

  # show tic tac toe board
  print(f"""\n{full_grid}""")


  # ----------------------
  # these are the winning combinations
  winning_combinations = [
    ["a1", "a2", "a3"],
    ["b1", "b2", "b3"],
    ["c1", "c2", "c3"],
    ["a1", "b1", "c1"],
    ["a2", "b2", "c2"],
    ["a3", "b3", "c3"],
    ["a1", "b2", "c3"],
    ["a3", "b2", "c1"],
  ]

  # loop through each of these combinations and check to see if they exist in the dictionary
  for combo in winning_combinations:
    if game_over == False:
      x_total = 0
      o_total = 0

      # check to see that each cell contains an X or an O and NOT a " "
      for cell in combo:
        if tictactoe[cell] == "X":
          x_total += 1
        elif tictactoe[cell] == "O":
          o_total += 1

      if x_total == 3 or o_total == 3:
        print(f"{'Player 2 (O),' if x_player else 'Player 1 (X),'} wins!")
        game_over = True
  