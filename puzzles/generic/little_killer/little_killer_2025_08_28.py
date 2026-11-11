"""PuzzleMadness Little Killer Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 3, 6],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 8],
        [8, 0, 2, 0, 0, 0, 7, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (0, 7)], 9, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 25, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 31, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 26, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 21, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 13, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 35, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 33, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 24, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 14, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 50, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 7, clue_position=(1, 2, 0))

    return puzzle
