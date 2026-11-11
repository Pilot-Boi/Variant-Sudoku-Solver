"""PuzzleMadness Little Killer Sudoku — 2025-10-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 6, 1, 0],
        [0, 9, 0, 0, 3, 0, 0, 0, 5],
        [0, 6, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 8, 0, 0, 0, 3, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 0, 0, 5, 3, 0],
        [8, 0, 1, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 24, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 31, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 23, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 9, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 18, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 32, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 28, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 25, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 8, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 52, clue_position=(1, 9, 2))

    return puzzle
