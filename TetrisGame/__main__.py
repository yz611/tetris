from pathlib import Path
from TetrisGame.board import Board


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
