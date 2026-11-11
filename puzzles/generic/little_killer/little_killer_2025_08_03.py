"""PuzzleMadness Little Killer Sudoku — 2025-08-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 6],
        [2, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [7, 2, 1, 0, 0, 0, 6, 0, 0],
        [8, 0, 3, 0, 0, 6, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 8, 0, 7, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 30, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 29, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 20, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 25, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 37, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 10, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 24, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 21, clue_position=(0, 4, 0))

    return puzzle
