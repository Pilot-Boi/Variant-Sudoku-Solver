"""PuzzleMadness Little Killer Sudoku — 2025-12-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 0, 0, 0, 0],
        [9, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 9, 0],
        [0, 4, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 6, 0, 0, 0, 0, 7, 5],
        [7, 5, 8, 0, 0, 0, 1, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 29, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 19, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 18, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 30, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 18, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 37, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 26, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 17, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 34, clue_position=(1, 6, 2))

    return puzzle
