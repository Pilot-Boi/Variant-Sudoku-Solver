"""PuzzleMadness Little Killer Sudoku — 2025-11-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 4, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 1, 5, 0],
        [0, 7, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 2, 0, 7, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 2, 0, 0, 7, 0],
        [8, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 46, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 12, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 15, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 34, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 30, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 10, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 10, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 19, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 53, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 28, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 12, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 36, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 26, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 56, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 29, clue_position=(0, 3, 1))

    return puzzle
