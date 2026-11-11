"""PuzzleMadness Little Killer Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 1, 3, 5, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 4, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 3, 0, 0, 2, 0, 7, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 55, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(1, 8), (0, 7)], 8, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 26, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 40, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 32, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 17, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 9, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 51, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 28, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 32, clue_position=(0, 2, 3))

    return puzzle
