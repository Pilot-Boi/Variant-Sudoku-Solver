"""PuzzleMadness Little Killer Sudoku — 2025-07-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 7, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 3, 0, 2, 0],
        [0, 0, 4, 0, 0, 9, 0, 0, 3],
        [0, 0, 0, 0, 6, 5, 9, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 19, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 31, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 35, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 24, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 31, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 26, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 33, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 22, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 27, clue_position=(1, 9, 0))

    return puzzle
