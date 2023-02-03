import unittest

from ShipGame import ShipGame


class MyTestCase(unittest.TestCase):
    def test_can_shipgame_class_make_shipgame_object(self):
        s = ShipGame()
        self.assertIsInstance(s, ShipGame)
        # pass

    def test_can_shipgame_class_enforce_first_turn_order(self):
        s = ShipGame()
        turn = s.whose_turn()
        self.assertEqual(turn, "second")
        # pass

    def test_can_shipgame_class_enforce_second_turn_order(self):
        s = ShipGame()
        s.fire_torpedo("first", "A10")
        s.fire_torpedo("second", "A9")
        s.fire_torpedo("first", "B5")
        new_turn = s.whose_turn()
        self.assertTrue(new_turn, "second")
        # pass

    def test_can_shipgame_fire_torpedo_enforce_turn_order(self):
        s = ShipGame()
        s.fire_torpedo("first", "A9")
        s.fire_torpedo("second", "A10")
        s.fire_torpedo("first", "B5")
        new_turn = s.fire_torpedo("first", "B10")
        self.assertFalse(new_turn)
        # pass

    def test_can_place_ship_check_invalid_ship_length_lessthan_2(self):
        s = ShipGame()
        invalid_place = s.place_ship("second", 0, "A10", "C")
        self.assertFalse(invalid_place)
        # pass

    def test_for_out_of_bounds_c_ship_placement_p1(self):
        s = ShipGame()
        out_of_bound = s.place_ship("first", 5, "H10", "C")
        self.assertFalse(out_of_bound)
        # pass

    def test_to_add_ship_for_p1(self):
        s = ShipGame()
        add_ship = s.place_ship("first", 4, "C5", "C")
        self.assertEqual(add_ship, True)
        # pass

    def test_adding_out_of_bounds_r_ship_placement_p1(self):
        s = ShipGame()
        out_of_bound = s.place_ship("first", 10, "A5", "R")
        self.assertFalse(out_of_bound)
        # pass

    def test_add_ship_for_p2(self):
        s = ShipGame()
        add_ship = s.place_ship("second", 4, "C5", "C")
        self.assertEqual(add_ship, True)
        # pass

    def test_adding_out_of_bounds_r_ship_placement_p2(self):
        s = ShipGame()
        out_of_bound = s.place_ship("second", 10, "A5", "R")
        self.assertFalse(out_of_bound)
        # pass

    def test_adding_out_of_bounds_c_ship_placement_p2(self):
        s = ShipGame()
        out_of_bound = s.place_ship("second", 5, "H10", "R")
        self.assertFalse(out_of_bound)
        # pass

    def test_adding_overlapping_ship_placement(self):
        s = ShipGame()
        s.place_ship("first", 5, "B2", "R")
        overlapping = s.place_ship("first", 4, "B2", "C")
        self.assertFalse(overlapping)
        # pass

    def test_adding_overlapping_ship_placement_c(self):
        s = ShipGame()
        s.place_ship("first", 4, "A5", "R")
        s.place_ship("first", 3, "A6", "C")
        overlapping = s.place_ship("first", 3, "A6", "R")
        self.assertFalse(overlapping)
        # pass

    def test_can_add_overlapping_ship_placement_r(self):
        s = ShipGame()
        s.place_ship("second", 4, "B5", "R")
        overlapping = s.place_ship("second", 3, "B7", "R")
        self.assertFalse(overlapping)
        # pass

    def test_can_fire_torpedo_enforce_turn_order(self):
        game = ShipGame()
        game.fire_torpedo("first", "A10")
        game.fire_torpedo("second", "B5")
        game.fire_torpedo("first", "C9")
        not_right_turn = game.fire_torpedo("first", "A5")
        self.assertFalse(not_right_turn)
        # pass

    def test_update_current_state_when_torpedo_resulted_in_win_p1(self):
        s = ShipGame()
        s.place_ship("first", 3, "A2", "C")
        s.place_ship("second", 3, "B5", "R")
        s.place_ship("first", 4, "C3", "R")
        s.fire_torpedo("first", "A2")
        s.fire_torpedo("second", "C4")
        s.fire_torpedo("first", "B5")
        s.fire_torpedo("second", "B2")
        s.fire_torpedo("first", "B6")
        s.fire_torpedo("second", "C2")
        s.fire_torpedo("first", "B7")
        final_move = s.get_current_state()
        self.assertEqual(final_move, "FIRST_WON")

    def test_can_get_num_ships_remaining_for_player(self):
        s = ShipGame()
        s.place_ship("first", 3, "A2", "C")
        s.place_ship("first", 4, "B4", "R")
        ships_remaining = s.get_num_ships_remaining("first")
        self.assertEqual(ships_remaining, 2)

    def test_can_ship_return_unfinished_when_no_ships_on_players_grid(self):
        game = ShipGame()
        game.place_ship("second", 4, 'A4', 'R')
        game.place_ship("second", 3, 'B2', 'C')
        game.fire_torpedo("first", "H2")
        game.fire_torpedo("second", "I8")
        game.fire_torpedo("first", "C5")
        game.fire_torpedo("second", "I9")
        current_state = game.get_current_state()
        self.assertEqual(current_state, "UNFINISHED")