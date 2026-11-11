"""PuzzleMadness Little Killer Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 5, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 7, 0, 2, 1, 0],
        [0, 1, 0, 3, 9, 0, 0, 0, 0],
        [0, 7, 4, 0, 0, 0, 0, 0, 8],
        [8, 9, 0, 0, 0, 2, 0, 0, 0],
        [0, 6, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 5, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 11, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 25, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 23, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 52, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 25, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 47, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 27, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 49, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 14, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 41, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 32, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 47, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 29, clue_position=(0, 1, 2))

    return puzzle
