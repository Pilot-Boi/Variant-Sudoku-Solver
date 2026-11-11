"""PuzzleMadness Little Killer Sudoku — 2025-01-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 5, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 8, 7, 0, 6, 0, 0, 0],
        [0, 3, 4, 0, 0, 0, 0, 6, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 5, 0, 0, 0, 0, 1],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 48, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 26, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 17, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 43, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 30, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 40, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 46, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 28, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 15, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 30, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 28, clue_position=(0, 3, 3))

    return puzzle
