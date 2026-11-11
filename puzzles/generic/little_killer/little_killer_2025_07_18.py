"""PuzzleMadness Little Killer Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 8, 9],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 9, 0, 6, 5, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 4, 6],
        [9, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 6, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 21, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 18, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 25, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 56, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 39, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 42, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 48, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 10, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 22, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 15, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 13, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 36, clue_position=(1, 9, 0))

    return puzzle
