"""PuzzleMadness Little Killer Sudoku — 2025-04-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 5, 7, 0, 0],
        [8, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 5, 7, 9, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 7, 6],
        [0, 0, 0, 0, 2, 1, 0, 0, 0],
        [5, 0, 0, 0, 0, 7, 6, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 27, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 8, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 26, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 9, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 34, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 45, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 26, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 20, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 40, clue_position=(0, 2, 2))

    return puzzle
