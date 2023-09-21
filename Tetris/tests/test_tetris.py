from unittest import TestCase
from Tetris.__main__ import Board


class TestTetris(TestCase):

    def setUp(self) -> None:
        self.board = Board()

    def test_Q0(self):
        command = "Q0"
        self.board.put_piece(command[0], command[1])
        self.assertEqual(self.board.max_height, 2)

    def tearDown(self) -> None:
        self.board.clear()

    def test_I0_I4_Q8(self):
        row = "I0,I4,Q8"
        for command in row.split(","):
            self.board.put_piece(command[0], command[1])
        self.assertEqual(self.board.max_height, 1)

    def test_T1_Z3_I4(self):
        row = "T1,Z3,I4"
        for command in row.split(","):
            self.board.put_piece(command[0], command[1])
        self.assertEqual(self.board.max_height, 4)

    def test_Q0_I2_I6_I0_I6_I6_Q2_Q4(self):
        row = "Q0,I2,I6,I0,I6,I6,Q2,Q4"
        for command in row.split(","):
            self.board.put_piece(command[0], command[1])
        self.assertEqual(self.board.max_height, 3)