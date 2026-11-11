"""PuzzleMadness Little Killer Sudoku — 2025-09-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 5, 9, 1],
        [0, 0, 6, 0, 0, 5, 4, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 1, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 7), (7, 8)], 8, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 45, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 21, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 24, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 10, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 44, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 8, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 38, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 31, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 35, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 7, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 20, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 45, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 42, clue_position=(0, 0, 2))

    return puzzle
