"""PuzzleMadness Little Killer Sudoku — 2025-10-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 0, 5],
        [0, 2, 0, 0, 6, 0, 7, 0, 0],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 7, 0, 0, 0, 0],
        [1, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 28, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 13, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 12, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 17, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 21, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 16, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 50, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 26, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 13, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 27, clue_position=(0, 2, 2))

    return puzzle
