from pathlib import Path

BOARD_WIDTH = 10
BOARD_HEIGHT = 10


piece_position_map = {
    'Q': [(0, 0), (0, 1), (1, 1), (1, 0)],
    'Z': [(0, 1), (1, 1), (1, 0), (2, 0)],
    'S': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'T': [(0, 1), (1, 1), (1, 0), (2, 1)],
    'I': [(0, 0), (1, 0), (2, 0), (3, 0)],
    'L': [(0, 0), (0, 1), (0, 2), (1, 0)],
    'J': [(0, 0), (1, 0), (1, 1), (1, 2)]
}


class Board:

    def __init__(self):
        self._board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.max_height_map = [0 for _ in range(BOARD_WIDTH)]
        self.max_width_map = [0 for _ in range(BOARD_HEIGHT)]

    def __str__(self):
        board_repr = "\n".join([
            str([self._board[j][i] for i in range(len(self._board))])
            for j in range(len(self._board[0])-1, -1, -1)
        ])
        return board_repr

    def clear(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                self._board[i][j] = 0
        self.max_height_map = [0 for _ in range(BOARD_WIDTH)]
        self.max_width_map = [0 for _ in range(BOARD_HEIGHT)]

    def place_piece(self, piece: str, start_col: str):
        positions = piece_position_map[piece]
        start_col = int(start_col)
        start_row = self.max_height_map[start_col]
        for x, y in positions:
            col = x + start_col
            row = y + start_row
            self._board[row][col] = 1
            self.max_height_map[col] += 1
            self.max_width_map[row] += 1
            if self.max_width_map[row] == BOARD_WIDTH:
                self.remove_row_and_update_maps(row)

    def remove_row_and_update_maps(self, idx: int):
        del self._board[idx]
        self._board.append([0 for _ in range(BOARD_WIDTH)])

        del self.max_width_map[idx]
        self.max_width_map.append(0)

        self.max_height_map = [i-1 for i in self.max_height_map]


def main():
    input_file = Path(__file__).parent.parent / "test_input.txt"  # Replace with your CSV file
    reader = (row for row in open(input_file, 'r'))
    board = Board()
    for row in reader:
        commands = row.strip().split(",")
        for command in commands:
            board.place_piece(command[0], command[1])
            print(board)
            print()
        print(max(board.max_height_map))

        board.clear()


if __name__ == "__main__":
    main()
