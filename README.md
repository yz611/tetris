# Tetris
A simple implementation of tetris.

## Introduction
A simplified tetris game, no rotations or horizontal movements considered. 

The program processes a text file of lines each representing a sequence of pieces entering the grid. 
For each line of the input file, your program should output the resulting height of the remaining blocks within the grid.
The file denotes the different possible shapes by letter. The letters used are Q, Z, S, T, I, L, and J, which are mapped to
positions (with upper-left corner being (0, 0) in each case).
```py
piece_position_map = {
    "Q": [[0, 0], [1, 0], [1, -1], [0, -1]],
    "Z": [[0, 0], [1, 0], [1, -1], [2, -1]],
    "S": [[2, 0], [1, 0], [1, -1], [0, -1]],
    "T": [[0, 0], [1, 0], [2, 0], [1, -1]],
    "I": [[0, 0], [1, 0], [2, 0], [3, 0]],
    "L": [[0, 0], [0, -1], [0, -2], [1, -2]],
    "J": [[1, 0], [1, -1], [1, -2], [0, -2]],
}
```

## Examples

* If the line is "Q0". The output should be 2.
* If the line is "Q0,Q2,Q4,Q6,Q8". The output should be 0.
* If the line is "I0,I4,Q8". The output should be 1.


## Testing
To test:
```shell
chmod +x run_tests
./run_tests
```

## Use:
To output:
```shell
chmod +x tetris
./tetris < input.txt > output.txt
```