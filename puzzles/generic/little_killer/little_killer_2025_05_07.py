"""PuzzleMadness Little Killer Sudoku — 2025-05-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 9, 0, 0],
        [9, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 1, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 7, 0],
        [4, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 37, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 37, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 30, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 15, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 28, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 37, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 37, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 40, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 24, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 13, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 44, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 28, clue_position=(1, 9, 0))

    return puzzle
