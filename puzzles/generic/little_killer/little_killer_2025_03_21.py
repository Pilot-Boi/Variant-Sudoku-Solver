"""PuzzleMadness Little Killer Sudoku — 2025-03-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 6, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 4, 7, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [5, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 0, 4, 6, 0, 0],
        [0, 0, 0, 5, 8, 2, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 56, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 39, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 11, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 35, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 5, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 25, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 28, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 35, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 27, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 21, clue_position=(1, 5, 3))

    return puzzle
