"""PuzzleMadness Little Killer Sudoku — 2025-02-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [6, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 8, 0],
        [9, 0, 5, 0, 0, 0, 0, 0, 3],
        [8, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 0, 7, 2, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 41, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 37, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 32, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 13, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 43, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 29, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 9, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 17, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 15, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 28, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 37, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 23, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 20, clue_position=(0, 2, 3))

    return puzzle
