"""PuzzleMadness Little Killer Sudoku — 2025-10-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 1, 2, 0, 0, 0, 0],
        [0, 0, 9, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 4, 0, 0],
        [0, 6, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 7],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 8), (8, 7)], 13, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 46, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 25, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 12, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 11, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 10, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 14, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 47, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 28, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 23, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 37, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 20, clue_position=(1, 4, 1))

    return puzzle
