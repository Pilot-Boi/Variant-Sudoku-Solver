"""PuzzleMadness Little Killer Sudoku — 2025-07-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 9, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 9, 7, 0],
        [0, 0, 0, 1, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 3, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 9],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 10, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 14, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 6, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 37, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 17, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 36, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 1), (7, 0)], 9, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 19, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 38, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 43, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 11, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 18, clue_position=(0, 4, 2))

    return puzzle
