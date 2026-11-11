"""PuzzleMadness Little Killer Sudoku — 2025-12-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 4, 0],
        [4, 0, 0, 0, 0, 6, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 3, 2],
        [5, 0, 0, 0, 0, 0, 6, 0, 0],
        [3, 1, 0, 0, 9, 8, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 43, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 23, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 28, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 34, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 29, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 18, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 37, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 14, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 25, clue_position=(1, 4, 1))

    return puzzle
