"""PuzzleMadness Little Killer Sudoku — 2025-05-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 3, 0, 0],
        [6, 0, 0, 0, 0, 0, 1, 2, 0],
        [1, 0, 0, 0, 0, 3, 0, 0, 0],
        [5, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 6, 0],
        [0, 0, 7, 1, 0, 0, 0, 3, 0],
        [9, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 25, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 28, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 9, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 13, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 22, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 14, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 12, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 14, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 8, clue_position=(1, 4, 2))

    return puzzle
