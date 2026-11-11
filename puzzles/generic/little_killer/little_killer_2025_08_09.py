"""PuzzleMadness Little Killer Sudoku — 2025-08-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 5],
        [0, 0, 0, 3, 4, 0, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [0, 0, 0, 5, 6, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 21, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 37, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 17, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 37, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 28, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 54, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 11, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 34, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 9, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 14, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 40, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 3, clue_position=(1, 2, 3))

    return puzzle
