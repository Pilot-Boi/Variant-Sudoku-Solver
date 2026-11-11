"""PuzzleMadness Little Killer Sudoku — 2025-02-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 5, 0, 0, 0, 0],
        [0, 5, 1, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 3, 0],
        [8, 0, 3, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 38, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 31, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(1, 8), (0, 7)], 16, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 13, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 27, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 21, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 15, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 42, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 22, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 39, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 9, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 28, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 19, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 39, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 42, clue_position=(0, -1, 2))

    return puzzle
