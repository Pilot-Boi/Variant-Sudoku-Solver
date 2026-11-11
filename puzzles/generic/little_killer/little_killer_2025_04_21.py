"""PuzzleMadness Little Killer Sudoku — 2025-04-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 4, 6, 0, 8, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 8, 9, 0, 0],
        [0, 0, 9, 0, 0, 5, 0, 6, 0],
        [0, 0, 0, 0, 0, 6, 7, 0, 0],
        [0, 0, 0, 7, 0, 0, 1, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 10, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 31, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(1, 0), (0, 1)], 14, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 21, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 36, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 30, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 41, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 37, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 46, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 11, clue_position=(1, 3, 2))

    return puzzle
