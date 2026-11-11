"""PuzzleMadness Little Killer Sudoku — 2025-09-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 1, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 8, 0, 0, 7, 0, 9],
        [0, 0, 0, 0, 0, 8, 1, 0, 5],
        [0, 0, 0, 0, 7, 0, 0, 0, 8],
        [0, 0, 0, 3, 0, 0, 0, 7, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 14, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 14, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 13, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 29, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 43, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 8, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 40, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 35, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 38, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 13, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 32, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 48, clue_position=(1, 7, 1))

    return puzzle
