from copy import deepcopy
from pathlib import Path

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

    def __init__(self):
        self._board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.max_width_map = [0 for _ in range(BOARD_HEIGHT)]

    def __str__(self):
        board_repr = "\n".join([
            str([self._board[j][i] for i in range(len(self._board))])
            for j in range(len(self._board[0])-1, -1, -1)
        ])
        return board_repr

    def valid(self, positions: list[list[int, int]]) -> bool:
        for col, row in positions:
            if col < 0 or col > BOARD_WIDTH-1 or row < 0 or row > BOARD_HEIGHT-1:
                return False
            if self._board[row][col] == 1:
                return False
        return True

    def clear(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                self._board[i][j] = 0
        self.max_width_map = [0 for _ in range(BOARD_HEIGHT)]

    def put_piece(self, piece: str, start_col: str):
        positions = deepcopy(piece_position_map[piece])
        start_col = int(start_col)
        for pos in positions:
            pos[0] += start_col
            pos[1] += BOARD_HEIGHT - 1

        while self.valid(positions):
            for pos in positions:
                pos[1] -= 1

        for pos in positions:
            pos[1] += 1

        for col, row in positions:
            self._board[row][col] = 1
            self.max_width_map[row] += 1
            if self.max_width_map[row] == BOARD_WIDTH:
                self.remove_row_and_update_width_map(row)

    def remove_row_and_update_width_map(self, idx: int):
        del self._board[idx]
        self._board.append([0 for _ in range(BOARD_WIDTH)])

        del self.max_width_map[idx]
        self.max_width_map.append(0)

    @property
    def max_height(self):
        max_height = 0
        for i in range(BOARD_WIDTH):
            for row in range(BOARD_HEIGHT - 1, -1, -1):
                if self._board[row][i] == 1:
                    max_height = max(max_height, row+1)
                    break
        return max_height


def main():
    input_file = Path(__file__).parent.parent / "input.txt"  # Replace with your CSV file
    reader = (row for row in open(input_file, 'r'))
    board = Board()
    for row in reader:
        commands = row.strip().split(",")
        for command in commands:
            board.put_piece(command[0], command[1])
        print(board.max_height)

        board.clear()


if __name__ == "__main__":
    main()
