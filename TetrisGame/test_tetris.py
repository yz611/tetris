from unittest import TestCase
from TetrisGame.board import Board


class TestTetris(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.board = Board(height=10)

    def tearDown(self) -> None:
        self.board.clear()

    def test_Q0(self):
        command = "Q0"
        self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 2)

    def test_Z0(self):
        command = "Z0"
        self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 2)

    def test_S0(self):
        command = "S0"
        self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 2)

    def test_T0(self):
        command = "S0"
        self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 2)

    def test_I0(self):
        command = "I0"
        self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 1)

    def test_L0(self):
        command = "L0"
        self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 3)

    def test_J0(self):
        command = "J0"
        self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 3)

    def test_over_height(self):
        for command in ["Q0"] * 52:
            self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 104)

    def test_out_of_right_bound(self):
        command = "L9"
        with self.assertRaises(IndexError):
            self.board.put_shape(command[0], command[1])

    def test_I0_I4_Q8(self):
        row = "I0,I4,Q8"
        for command in row.split(","):
            self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 1)

    def test_T1_Z3_I4(self):
        row = "T1,Z3,I4"
        for command in row.split(","):
            self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 4)

    def test_Q0_I2_I6_I0_I6_I6_Q2_Q4(self):
        row = "Q0,I2,I6,I0,I6,I6,Q2,Q4"
        for command in row.split(","):
            self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 3)

    def test_I0_I6_S4(self):
        row = "I0,I6,S4"
        for command in row.split(","):
            self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 1)

    def test_S0_S2_S4_S5_Q8_Q8_Q8_Q8_T1_Q1_I0_Q4(self):
        row = "S0,S2,S4,S5,Q8,Q8,Q8,Q8,T1,Q1,I0,Q4"
        for command in row.split(","):
            self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 8)

    def test_L0_J3_L5_J8_T1_T6_S2_Z5_T0_T7(self):
        row = "L0,J3,L5,J8,T1,T6,S2,Z5,T0,T7"
        for command in row.split(","):
            self.board.put_shape(command[0], command[1])
        self.assertEqual(self.board.max_height, 0)
