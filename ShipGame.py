# Author: Hanami Do
# Github Username: hanamilktea
# Date: 02/24/2022
# Description: Portfolio Project - Code for a Battleship game between two players;
# where players place ships on their grid, take turns
# firing torpedos at the opponent's grids, and the player wins
# when they sink their opponent's final ship.

class ShipGame:
    """A class that represents the Battleship game, played by two players.
    Player 1 ('first') always starts first. Has methods for players to
    place their ships, fire torpedos at the opponent's grid, get the
    current state of the game, and get the number of ships they still have."""

    def __init__(self):
        """Takes no parameters.
        Initializes private data members."""
        self._current_state = "UNFINISHED"
        self._current_turn = "first"
        self._player1_ships = []
        self._player2_ships = []
        self._player1_grid = {
            "A1": "",
            "A2": "",
            "A3": "",
            "A4": "",
            "A5": "",
            "A6": "",
            "A7": "",
            "A8": "",
            "A9": "",
            "A10": "",
            "B1": "",
            "B2": "",
            "B3": "",
            "B4": "",
            "B5": "",
            "B6": "",
            "B7": "",
            "B8": "",
            "B9": "",
            "B10": "",
            "C1": "",
            "C2": "",
            "C3": "",
            "C4": "",
            "C5": "",
            "C6": "",
            "C7": "",
            "C8": "",
            "C9": "",
            "C10": "",
            "D1": "",
            "D2": "",
            "D3": "",
            "D4": "",
            "D5": "",
            "D6": "",
            "D7": "",
            "D8": "",
            "D9": "",
            "D10": "",
            "E1": "",
            "E2": "",
            "E3": "",
            "E4": "",
            "E5": "",
            "E6": "",
            "E7": "",
            "E8": "",
            "E9": "",
            "E10": "",
            "F1": "",
            "F2": "",
            "F3": "",
            "F4": "",
            "F5": "",
            "F6": "",
            "F7": "",
            "F8": "",
            "F9": "",
            "F10": "",
            "G1": "",
            "G2": "",
            "G3": "",
            "G4": "",
            "G5": "",
            "G6": "",
            "G7": "",
            "G8": "",
            "G9": "",
            "G10": "",
            "H1": "",
            "H2": "",
            "H3": "",
            "H4": "",
            "H5": "",
            "H6": "",
            "H7": "",
            "H8": "",
            "H9": "",
            "H10": "",
            "I1": "",
            "I2": "",
            "I3": "",
            "I4": "",
            "I5": "",
            "I6": "",
            "I7": "",
            "I8": "",
            "I9": "",
            "I10": "",
            "J1": "",
            "J2": "",
            "J3": "",
            "J4": "",
            "J5": "",
            "J6": "",
            "J7": "",
            "J8": "",
            "J9": "",
            "J10": ""
        }
        self._player2_grid = {
            "A1": "",
            "A2": "",
            "A3": "",
            "A4": "",
            "A5": "",
            "A6": "",
            "A7": "",
            "A8": "",
            "A9": "",
            "A10": "",
            "B1": "",
            "B2": "",
            "B3": "",
            "B4": "",
            "B5": "",
            "B6": "",
            "B7": "",
            "B8": "",
            "B9": "",
            "B10": "",
            "C1": "",
            "C2": "",
            "C3": "",
            "C4": "",
            "C5": "",
            "C6": "",
            "C7": "",
            "C8": "",
            "C9": "",
            "C10": "",
            "D1": "",
            "D2": "",
            "D3": "",
            "D4": "",
            "D5": "",
            "D6": "",
            "D7": "",
            "D8": "",
            "D9": "",
            "D10": "",
            "E1": "",
            "E2": "",
            "E3": "",
            "E4": "",
            "E5": "",
            "E6": "",
            "E7": "",
            "E8": "",
            "E9": "",
            "E10": "",
            "F1": "",
            "F2": "",
            "F3": "",
            "F4": "",
            "F5": "",
            "F6": "",
            "F7": "",
            "F8": "",
            "F9": "",
            "F10": "",
            "G1": "",
            "G2": "",
            "G3": "",
            "G4": "",
            "G5": "",
            "G6": "",
            "G7": "",
            "G8": "",
            "G9": "",
            "G10": "",
            "H1": "",
            "H2": "",
            "H3": "",
            "H4": "",
            "H5": "",
            "H6": "",
            "H7": "",
            "H8": "",
            "H9": "",
            "H10": "",
            "I1": "",
            "I2": "",
            "I3": "",
            "I4": "",
            "I5": "",
            "I6": "",
            "I7": "",
            "I8": "",
            "I9": "",
            "I10": "",
            "J1": "",
            "J2": "",
            "J3": "",
            "J4": "",
            "J5": "",
            "J6": "",
            "J7": "",
            "J8": "",
            "J9": "",
            "J10": ""
        }

    def get_current_state(self):
        """Takes no parameters.
        Returns current state of the game:
        "FIRST_WON", "SECOND_WON", or "UNFINISHED" """
        # check for status of game
        return self._current_state

    def set_current_state(self, set_state=""):
        """Parameter: the state of the game
        Sets current state of the game to the appropriate state:
        'FIRST_WON', 'SECOND_WON', or 'UNFINISHED' """
        self._current_state = set_state

    def check_player1_invalid_ship(self, ship_length, ship_coord, ship_orientation):
        """Parameters:
            ship_length: length of ship
            ship_coord: coordinates of the square the ship will occupy
            ship_orientation: ship's orientation ('R' for horizontal placement or 'C' for vertical placement.)
        Checks for Invalid ship placement for Player 1.
        Returns True if ship does not fit on that player's grid, if it will
        overlap previously placed ships, or if length of ship is less than
        2 (invalid placement)."""
        # check if ship length is less than 2
        if ship_length < 2:
            return True
        # add out of range list for columns
        out_of_range_columns = list(range(90, 100))
        # out of range list for rows
        out_of_range_rows = list(range(9, 100, 10))

        # check if ship would fit entirely on player's grid
        # first confirm if ship can added to same column (vertically)
        if ship_orientation == "C":
            # create list for keys in player's grid
            player1_keys = list(self._player1_grid.keys())

            # check if ship would overlap other ships on player's grid
            check_coord = ship_coord
            for num in range(1, ship_length):
                if self._player1_grid.get(check_coord) == "X":
                    # print(ship_coord, "already taken!")
                    # print(self._player1_grid)
                    return True
                check_initial_coord = player1_keys.index(check_coord)
                # check if ship is out of bounds vertically
                if check_initial_coord in out_of_range_columns:
                    return True
                check_initial_coord += 10
                new_coord = player1_keys[check_initial_coord]
                check_coord = new_coord

            player1_ship = [ship_coord]
            # mark coordinates according to specified ship length
            for num in range(1, ship_length):
                # mark ship coordinates on player's grid with X
                self._player1_grid.update({ship_coord: "X"})
                initial_coord = player1_keys.index(ship_coord)
                initial_coord += 10
                update_coord = player1_keys[initial_coord]
                ship_coord = update_coord
                self._player1_grid.update({ship_coord: "X"})
                player1_ship.append(ship_coord)
            # print(self._player1_grid)
            self._player1_ships.append(player1_ship)
            # print(self._player1_ships)

        # confirm if ship can added to same row (horizontally)
        if ship_orientation == "R":
            # create list for keys in player's grid
            player1_keys = list(self._player1_grid.keys())

            # check if ship would overlap other ships on player's grid
            check_coord = ship_coord
            for num in range(1, ship_length):
                # check if ship is out of bounds horizontally
                if self._player1_grid.get(check_coord) == "X":
                    # print(ship_coord, "already taken!")
                    # print(self._player1_grid)
                    return True
                check_initial_coord = player1_keys.index(check_coord)
                # check of ship is out of bounds horizontally
                if check_initial_coord in out_of_range_rows:
                    return True
                check_initial_coord += 1
                new_coord = player1_keys[check_initial_coord]
                check_coord = new_coord

            player1_ship = [ship_coord]
            # mark coordinates according to specified ship length
            for num in range(1, ship_length):
                # mark ship coordinates on player's grid with X
                self._player1_grid.update({ship_coord: "X"})
                initial_coord = player1_keys.index(ship_coord)
                initial_coord += 1
                added_coord = player1_keys[initial_coord]
                ship_coord = added_coord
                self._player1_grid.update({ship_coord: "X"})
                player1_ship.append(ship_coord)
            # print(self._player1_grid)
            self._player1_ships.append(player1_ship)
            # print(self._player1_ships)
        return False

    def check_player2_invalid_ship(self, ship_length, ship_coord, ship_orientation):
        """Parameters:
            ship_length: length of ship
            ship_coord: coordinates of the square the ship will occupy
            ship_orientation: ship's orientation ('R' for horizontal or 'C' for vertical.)
        Checks for Invalid ship placement for Player 2.
        Returns True if ship does not fit on that player's grid, if it will
        overlap previously placed ships, or if length of ship is less than
        2 (invalid placement)."""
        # check if ship length is less than 2
        if ship_length < 2:
            return True
        # add out of range list for columns
        out_of_range_columns = list(range(90, 100))
        # out of range list for rows
        out_of_range_rows = list(range(9, 100, 10))

        # check if ship would fit entirely on player 2's grid
        # first confirm if ship can added to same column (vertically)
        if ship_orientation == "C":
            # create list for keys in player 2's grid
            player2_keys = list(self._player2_grid.keys())

            # check if ship would overlap other ships on player 2's grid
            check_coord = ship_coord
            for num in range(1, ship_length):
                if self._player2_grid.get(check_coord) == "X":
                    # print(ship_coord, "already taken!")
                    # print(self._player2_grid)
                    return True
                check_initial_coord = player2_keys.index(check_coord)
                # check if ship is out of bounds vertically
                if check_initial_coord in out_of_range_columns:
                    return True
                check_initial_coord += 10
                new_coord = player2_keys[check_initial_coord]
                check_coord = new_coord

            player2_ship = [ship_coord]
            # mark coordinates according to specified ship length
            for n in range(1, ship_length):
                # mark ship coordinates on player 2's grid with X
                self._player2_grid.update({ship_coord: "X"})
                initial_coord = player2_keys.index(ship_coord)
                initial_coord += 10
                update_coord = player2_keys[initial_coord]
                ship_coord = update_coord
                self._player2_grid.update({ship_coord: "X"})
                player2_ship.append(ship_coord)
            # print(self._player2_grid)
            self._player2_ships.append(player2_ship)
            # print(self._player2_ships)

        # confirm if ship can added to same row (horizontally)
        if ship_orientation == "R":
            # create list for keys in player's grid
            player2_keys = list(self._player2_grid.keys())

            check_coord = ship_coord
            # check if ship would overlap other ships on player's grid
            for num in range(1, ship_length):
                if self._player2_grid.get(check_coord) == "X":
                    # print(ship_coord, "already taken!")
                    # print(self._player2_grid)
                    return True
                check_initial_coord = player2_keys.index(check_coord)
                # check if ship is out of bounds horizontally
                if check_initial_coord in out_of_range_rows:
                    return True
                check_initial_coord += 1
                new_coord = player2_keys[check_initial_coord]
                check_coord = new_coord

            player2_ship = [ship_coord]
            # mark coordinates according to specified ship length
            for num in range(1, ship_length):
                # mark ship coordinates on player 2's grid with X
                self._player2_grid.update({ship_coord: "X"})
                initial_coord = player2_keys.index(ship_coord)
                initial_coord += 1
                added_coord = player2_keys[initial_coord]
                ship_coord = added_coord
                # print(ship_coord)
                self._player2_grid.update({ship_coord: "X"})
                player2_ship.append(ship_coord)
            # print(self._player2_grid)
            self._player2_ships.append(player2_ship)
            # print(self._player2_ships)
        return False

    def place_ship(self, player_num, ship_length, ship_coord, ship_orientation):
        """
        Parameters:
            player_num: "first" or "second"
            ship_length: length of ship
            ship_coord: coordinates of the square the ship will occupy
            ship_orientation: ship's orientation ('R' for horizontal placement, or 'C' for vertical placement)
        Calls check_player1_invalid_ship or check_player2_invalid_ship to check if it is a valid ship placement.
        Returns: False if invalid placement; True if valid placement
        """
        # validate ship placement for player 1
        if player_num == "first":
            # print("Player 1's grid: ")
            if self.check_player1_invalid_ship(ship_length, ship_coord, ship_orientation):
                return False

        # validate ship placement for player 2
        if player_num == "second":
            # print("Player 2's grid")
            if self.check_player2_invalid_ship(ship_length, ship_coord, ship_orientation):
                return False
        return True

    def whose_turn(self):
        """Takes no parameters. Keeps track of current turn.
        Returns current player's turn."""
        # if current_turn is first, then update turn to second
        if self._current_turn == "first":
            self._current_turn = "second"
        # if current_turn is second, then update turn to first
        else:
            self._current_turn = "first"
        return self._current_turn

    def fire_torpedo(self, player_num, torpedo_coord):
        """
        Parameters:
            player_num: the player
            torpedo_coord: target coordinates.
        Checks validity of move.
        Returns False if invalid torpedo.
        Returns True; then records move, update whose turn it is, update the current state (if this
        turn sank the opponent's final ship), and return True.
        """
        # Check if it is NOT currently that player's turn
        if self._current_turn != player_num:
            return False
        # Check if game has already been won
        elif self._current_state != "UNFINISHED":
            return False

        # validate move for player 1
        if player_num == "first":
            if torpedo_coord in self._player2_grid.keys():
                # removes torpedoed coordinate
                # adds "H" for Hit
                self._player2_grid[torpedo_coord] = "H"
                # print(torpedo_coord, "has been hit")
            for ship in self._player2_ships:
                # Removes coordinate from ship once hit
                if torpedo_coord in ship:
                    ship.remove(torpedo_coord)
                    # print(self._player2_ships)
            # if no ships have been added yet
            if not self._player2_ships:
                print("Please try adding a ship first")
            # Update current state if move resulted in a win
            elif all(ship == [] for ship in self._player2_ships):
                self.set_current_state("FIRST_WON")

        # validate move for player 2
        if player_num == "second":
            # Check if torpedo is legal move
            if torpedo_coord in self._player1_grid.keys():
                # removes torpedoed coordinate
                # adds "H" for Hit
                self._player1_grid[torpedo_coord] = "H"
                # print(torpedo_coord, "has been hit")
            for ship in self._player1_ships:
                # Remove coordinate from ship once hit
                if torpedo_coord in ship:
                    ship.remove(torpedo_coord)
                    # print(self._player1_ships)
            # if no ships have been added yet
            if not self._player1_ships:
                print("Please try adding a ship first")
            # Update current state if move resulted in a win
            elif all(ship == [] for ship in self._player1_ships):
                self.set_current_state("SECOND_WON")

        # updates turn if legal move
        self.whose_turn()
        return True

    def get_num_ships_remaining(self, player):
        """Parameter: player ('first' or 'second')
        Returns how many ships the specified player still has left."""
        counter = 0
        if player == "first":
            for ship in self._player1_ships:
                if len(ship) != 0:
                    counter += 1
        if player == "second":
            for ship in self._player2_ships:
                if len(ship) != 0:
                    counter += 1
        return counter