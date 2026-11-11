"""PuzzleMadness Little Killer Sudoku — 2025-03-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 1, 2, 8, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [8, 5, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 1, 0, 9, 0],
        [1, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (0, 7)], 12, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 23, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 23, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 44, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 26, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 21, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 17, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 13, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 7, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 48, clue_position=(1, 7, 2))

    return puzzle
