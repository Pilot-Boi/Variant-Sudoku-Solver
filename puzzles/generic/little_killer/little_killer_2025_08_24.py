"""PuzzleMadness Little Killer Sudoku — 2025-08-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 3, 0, 0, 1, 2],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [2, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 9, 4, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [3, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 6, 0, 5, 0, 0, 7, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 4, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 22, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 39, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 15, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 15, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 35, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 32, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 31, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 35, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 27, clue_position=(1, 7, 0))

    return puzzle
