"""PuzzleMadness Little Killer Sudoku — 2025-11-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 6, 0, 0],
        [0, 9, 0, 0, 0, 6, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [1, 7, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 4, 5, 0, 2],
        [0, 0, 0, 0, 0, 3, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 0), (8, 1)], 11, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 20, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 13, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 16, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 18, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 42, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 45, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 21, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 26, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 14, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 30, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 1), (1, 0)], 9, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 23, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 45, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 38, clue_position=(0, 2, 1))

    return puzzle
