"""PuzzleMadness Little Killer Sudoku — 2025-03-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 4, 0, 2, 6, 0, 5],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 1, 0, 0],
        [0, 0, 0, 2, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 27, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 34, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 10, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 21, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 6, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 41, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 12, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 52, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 15, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 52, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 32, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 34, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 28, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 44, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 23, clue_position=(0, 3, 1))

    return puzzle
