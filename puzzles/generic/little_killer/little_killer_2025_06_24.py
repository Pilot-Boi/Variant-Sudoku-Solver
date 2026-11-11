"""PuzzleMadness Little Killer Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 1, 0, 6, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 4, 0, 9],
        [0, 0, 9, 0, 0, 0, 0, 0, 1],
        [0, 0, 4, 0, 0, 0, 5, 0, 0],
        [4, 5, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 7), (7, 8)], 5, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 32, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 38, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 46, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 38, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 42, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 32, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 30, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 45, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 5, clue_position=(1, 2, 2))

    return puzzle
