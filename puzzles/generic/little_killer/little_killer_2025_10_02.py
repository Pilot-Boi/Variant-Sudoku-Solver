"""PuzzleMadness Little Killer Sudoku — 2025-10-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 9, 0, 5, 0, 0, 0, 0, 0],
        [0, 3, 4, 7, 0, 2, 1, 5, 0],
        [0, 7, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 8],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 41, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 28, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 40, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 38, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 34, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 9, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 21, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 37, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 15, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 23, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(1, 8), (0, 7)], 8, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 23, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 33, clue_position=(1, 8, 3))

    return puzzle
