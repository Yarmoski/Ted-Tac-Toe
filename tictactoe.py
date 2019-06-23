line1 = ["-", "-", "-"]
line2 = ["-", "-", "-"]
line3 = ["-", "-", "-"]
game_in_progress = True

turn_counter = 0

def display_board():
  print("===========================================================")
  print("\n\nThis is the current Tic Tac Toe board: \n\n")
  print(line1)
  print(line2)
  print(line3)

def invalid_choice_x():
  display_board()
  print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
  x_row = None
  x_index = None

def invalid_choice_o():
  display_board()
  print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
  o_row = None
  o_index = None


def x_turn():
  print("\n\nIt is now the X player's turn!\n\n")
  global turn_counter
  x_row = None
  x_index = None

  while x_row not in range(1,4) or x_index not in range(0,3):
    print("Please enter a number from 1-3 for both questions:")
    x_row = int(input("What row would you like to select? "))
    x_index = int(input("What column would you like to select? ")) - 1
    if x_row == 1:
      if line1[x_index] != "X" and line1[x_index] != "O":
        line1[x_index] = "X"
      else:
        display_board()
        print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
        x_row = None
        x_index = None
    elif x_row == 2:
      if line2[x_index] != "X" and line2[x_index] != "O":
        line2[x_index] = "X"
      else:
        display_board()
        print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
        x_row = None
        x_index = None
    elif x_row == 3:
      if line3[x_index] != "X" and line3[x_index] != "O":
        line3[x_index] = "X"
      else:
        display_board()
        print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
        x_row = None
        x_index = None
    else:
      display_board()
      print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
      x_row = None
      x_index = None
  turn_counter += 1

def o_turn():
  print("\n\nIt is now the O player's turn!\n\n")
  global turn_counter
  o_row = None
  o_index = None

  while o_row not in range(1,4) or o_index not in range(0,3):
    print("Please enter a number from 1-3 for both questions:")
    o_row = int(input("What row would you like to select? "))
    o_index = int(input("What column would you like to select? ")) - 1
    if o_row == 1:
      if line1[o_index] != "X" and line1[o_index] != "O":
        line1[o_index] = "O"
      else:
        display_board()
        print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
        o_row = None
        o_index = None
    elif o_row == 2:
      if line2[o_index] != "X" and line2[o_index] != "O":
        line2[o_index] = "O"
      else:
        display_board()
        print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
        o_row = None
        o_index = None
    elif o_row == 3:
      if line3[o_index] != "X" and line3[o_index] != "O":
        line3[o_index] = "O"
      else:
        display_board()
        print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
        o_row = None
        o_index = None
    else:
      display_board()
      print("\n\n!!YOUR CHOICE WAS INVALID!! Please enter a valid choice.\n\n")
      x_row = None
      x_index = None

  turn_counter += 1



while game_in_progress:
  display_board()
  x_turn()
  # if someone wins or the whole board is filled, end the game
  if (line1[0] == line2[0] == line3[0] == ("X" or "O")) or (line1[1] == line2[1] == line3[1] == ("X" or "O")) or (line1[2] == line2[2] == line3[2] == ("X" or "O")) or (line1[0] == line1[1] == line1[2] == ("X" or "O")) or (line2[0] == line2[1] == line2[2] == ("X" or "O")) or (line3[0] == line3[1] == line3[2] == ("X" or "O")) or (line1[0] == line2[1] == line3[2] == ("X" or "O")) or (line1[2] == line2[1] == line3[0] == ("X" or "O")):
    game_in_progress = False
    print("Game over! Congratulations to the winner!")
    display_board()
    break
  if turn_counter >= 9:
    game_in_progress = False
    display_board()
    print("Game over! It was a tie!")
    break
  display_board()
  o_turn()
  #check if game is completed again
  if (line1[0] == line2[0] == line3[0] == ("X" or "O")) or (line1[1] == line2[1] == line3[1] == ("X" or "O")) or (line1[2] == line2[2] == line3[2] == ("X" or "O")) or (line1[0] == line1[1] == line1[2] == ("X" or "O")) or (line2[0] == line2[1] == line2[2] == ("X" or "O")) or (line3[0] == line3[1] == line3[2] == ("X" or "O")) or (line1[0] == line2[1] == line3[2] == ("X" or "O")) or (line1[2] == line2[1] == line3[0] == ("X" or "O")):
    game_in_progress = False
    print("Game over! Congratulations to the winner!")
    display_board()
    break
  if turn_counter >= 9:
    game_in_progress = False
    display_board()
    print("Game over! It was a tie!")
    break
