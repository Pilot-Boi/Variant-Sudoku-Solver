"""PuzzleMadness Little Killer Sudoku — 2025-05-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 7, 0, 0, 0, 0, 0],
        [3, 0, 2, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 5],
        [0, 0, 4, 0, 0, 0, 2, 0, 0],
        [1, 0, 0, 0, 0, 8, 0, 0, 0],
        [2, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 2, 0, 0, 6, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 18, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 16, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 14, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 16, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 42, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 45, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 35, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 15, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 43, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(8, 1), (7, 0)], 10, clue_position=(1, 2, 2))

    return puzzle
