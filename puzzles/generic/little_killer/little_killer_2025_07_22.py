"""PuzzleMadness Little Killer Sudoku — 2025-07-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [8, 0, 0, 4, 0, 2, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [2, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 36, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 31, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(0, 7), (1, 8)], 4, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 29, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 11, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 34, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 9, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 37, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 18, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 29, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 17, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 20, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 27, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 39, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 30, clue_position=(0, 2, 1))

    return puzzle
