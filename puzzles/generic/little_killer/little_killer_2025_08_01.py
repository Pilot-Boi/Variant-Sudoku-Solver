"""PuzzleMadness Little Killer Sudoku — 2025-08-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 7, 0, 0, 0, 0, 6, 0, 0],
        [0, 3, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 2, 0],
        [0, 0, 0, 8, 0, 2, 5, 0, 0],
        [0, 0, 7, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 34, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 20, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 36, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 14, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 27, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 15, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 14, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 33, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 32, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 10, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 37, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 38, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 10, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 50, clue_position=(0, -1, 2))

    return puzzle
