"""PuzzleMadness Little Killer Sudoku — 2025-09-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 2, 6, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 8, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 42, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 19, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 9, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 14, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 59, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 38, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 33, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 15, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 24, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 22, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 34, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 21, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 40, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 42, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 8, clue_position=(1, 3, 3))

    return puzzle
