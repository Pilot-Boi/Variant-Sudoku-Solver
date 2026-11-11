"""PuzzleMadness Little Killer Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 9, 0],
        [0, 0, 5, 0, 0, 3, 0, 0, 1],
        [0, 2, 0, 4, 0, 6, 7, 0, 0],
        [0, 6, 7, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 33, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 11, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 49, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 30, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 38, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 34, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 21, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 34, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 36, clue_position=(1, 8, 2))

    return puzzle
