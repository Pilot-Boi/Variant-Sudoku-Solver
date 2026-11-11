"""PuzzleMadness Little Killer Sudoku — 2025-11-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 0],
        [2, 1, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 9, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 1, 9, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 32, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 14, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 22, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 26, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 10, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 33, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 40, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 52, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 25, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 30, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 34, clue_position=(0, 4, 0))

    return puzzle
