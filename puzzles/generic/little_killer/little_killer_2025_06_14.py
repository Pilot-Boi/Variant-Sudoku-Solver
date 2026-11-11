"""PuzzleMadness Little Killer Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 2, 3, 8],
        [6, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 1, 4],
        [4, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 5, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 10, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 31, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 42, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 13, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(8, 1), (7, 0)], 12, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 11, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 39, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 20, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 35, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 20, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 25, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 40, clue_position=(1, 8, 3))

    return puzzle
