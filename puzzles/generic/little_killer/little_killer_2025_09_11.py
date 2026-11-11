"""PuzzleMadness Little Killer Sudoku — 2025-09-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 4, 6, 0],
        [0, 0, 1, 0, 0, 3, 0, 2, 8],
        [0, 0, 0, 0, 1, 0, 9, 0, 0],
        [0, 0, 0, 0, 2, 9, 0, 0, 3],
        [8, 9, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 62, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 52, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 16, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 21, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 28, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 25, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 27, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 15, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 38, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 21, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 32, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 38, clue_position=(0, 0, 3))

    return puzzle
