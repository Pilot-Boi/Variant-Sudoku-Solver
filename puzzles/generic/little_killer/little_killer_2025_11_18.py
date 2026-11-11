"""PuzzleMadness Little Killer Sudoku — 2025-11-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 7, 3, 8, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 3, 4, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 6],
        [0, 0, 0, 0, 2, 6, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 1, 0, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 13, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 41, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 23, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 16, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 40, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 9, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 12, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 46, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 24, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 50, clue_position=(0, 1, 1))

    return puzzle
