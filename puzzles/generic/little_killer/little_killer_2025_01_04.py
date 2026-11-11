"""PuzzleMadness Little Killer Sudoku — 2025-01-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 7, 0, 3, 0, 0],
        [0, 9, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 4, 0, 2],
        [0, 0, 8, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 9, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 2, 0, 0, 4, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 25, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 29, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 27, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(1, 8), (0, 7)], 9, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 12, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 13, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 37, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 45, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 39, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 29, clue_position=(1, 8, 2))

    return puzzle
