"""PuzzleMadness Little Killer Sudoku — 2025-08-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [4, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 2, 0, 0],
        [0, 5, 0, 6, 9, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 15, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 16, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 16, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 16, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 36, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 9, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 42, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 49, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 27, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 18, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 13, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 12, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 36, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 40, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 17, clue_position=(0, 6, 1))

    return puzzle
