"""PuzzleMadness Little Killer Sudoku — 2025-02-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 8, 7, 0, 0, 0, 2, 9, 0],
        [0, 0, 6, 0, 4, 0, 7, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 3, 0],
        [0, 5, 0, 0, 9, 0, 0, 0, 0],
        [4, 0, 0, 0, 2, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 18, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 30, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 14, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 29, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 34, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 55, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 3, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 10, clue_position=(1, 4, 2))

    return puzzle
