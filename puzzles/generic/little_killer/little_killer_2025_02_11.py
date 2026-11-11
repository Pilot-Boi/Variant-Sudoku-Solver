"""PuzzleMadness Little Killer Sudoku — 2025-02-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 4, 0, 3, 0, 0],
        [0, 0, 0, 0, 8, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 9, 0, 0, 0, 8, 0],
        [0, 0, 0, 4, 0, 0, 7, 0, 6],
        [0, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 2, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 30, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 24, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 18, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 31, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 17, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 30, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 21, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 42, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(1, 8), (0, 7)], 14, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 42, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 16, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 36, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 21, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 28, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 7, clue_position=(0, 6, 1))

    return puzzle
