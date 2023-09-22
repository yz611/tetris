from copy import deepcopy


BOARD_WIDTH = 10
BOARD_HEIGHT = 100


piece_position_map = {
    'Q': [[0, 0], [1, 0], [1, -1], [0, -1]],
    'Z': [[0, 0], [1, 0], [1, -1], [2, -1]],
    'S': [[0, -1], [1, -1], [1, 0], [2, 0]],
    'T': [[0, 0], [1, 0], [1, -1], [2, 0]],
    'I': [[0, 0], [1, 0], [2, 0], [3, 0]],
    'L': [[0, 0], [0, -1], [0, -2], [1, -2]],
    'J': [[1, 0], [1, -1], [1, -2], [0, -2]]
}


class Board:

    def __init__(self, width: int = BOARD_WIDTH, height: int = BOARD_HEIGHT):
        self._board = [[0 for _ in range(width)] for _ in range(height)]
        self._width = width
        self._height = height
        self.start_height = height
        self.max_width_map = [0 for _ in range(height)]

    def __str__(self):
        board_repr = "\n".join([
            str(self._board[i]) for i in range(len(self._board)-1, -1, -1)
        ])

        return board_repr

    def valid(self, positions: list[list[int, int]]) -> bool:
        """ check if the positions are within bounds and if collision """
        for col, row in positions:
            if col < 0 or col > self._width-1 or row < 0 or row > self._height-1:
                return False
            if self._board[row][col] == 1:
                return False
        return True

    def clear(self):
        """ clear the board to init state """
        self._height = self.start_height
        self._board = [[0 for _ in range(self._width)] for _ in range(self._height)]
        self.max_width_map = [0 for _ in range(self._height)]

    def put_piece(self, piece: str, start_col: str):
        """ put a piece at the correct location """
        positions = deepcopy(piece_position_map[piece])
        start_col = int(start_col)
        for pos in positions:  # set start positions at top
            pos[0] += start_col
            pos[1] += self._height - 1

        if not self.valid(positions):
            for _ in range(self._height):
                self._board.append([0 for _ in range(self._width)])
                self.max_width_map.append(0)
            self._height *= 2  # double the height of matrix if initial positions invalid
            for pos in positions:
                pos[1] += 4  # pieces have height <= 4

        while self.valid(positions):  # piece falls from top until collision
            for pos in positions:
                pos[1] -= 1

        for pos in positions:  # rollback to last valid positions
            pos[1] += 1

        for col, row in positions:
            self._board[row][col] = 1
            self.max_width_map[row] += 1
            if self.max_width_map[row] == self._width:
                self.remove_row_and_update_width_map(row)

    def remove_row_and_update_width_map(self, idx: int):
        del self._board[idx]
        self._board.append([0 for _ in range(self._width)])

        del self.max_width_map[idx]
        self.max_width_map.append(0)

    @property
    def max_height(self):
        max_height = 0
        for i in range(self._width):
            for row in range(self._height - 1, -1, -1):
                if self._board[row][i] == 1:
                    max_height = max(max_height, row+1)
                    break
        return max_height
