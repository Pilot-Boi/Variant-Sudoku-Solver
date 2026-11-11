"""PuzzleMadness Little Killer Sudoku — 2025-03-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 1],
        [0, 7, 0, 0, 0, 0, 4, 3, 0],
        [3, 5, 0, 7, 0, 0, 2, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 5, 0, 0, 7, 0, 6, 0],
        [2, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 7), (1, 8)], 13, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 21, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 20, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 33, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 7, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 31, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 12, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 57, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(1, 0), (0, 1)], 11, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 22, clue_position=(1, 4, 0))

    return puzzle
