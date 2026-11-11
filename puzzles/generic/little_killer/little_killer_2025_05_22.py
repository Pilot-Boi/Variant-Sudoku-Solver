"""PuzzleMadness Little Killer Sudoku — 2025-05-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 7, 0, 0, 0, 0, 0, 0],
        [3, 0, 2, 0, 9, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 1, 0, 0, 4, 0, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
        [8, 0, 0, 4, 0, 2, 0, 5, 0],
        [0, 0, 0, 6, 7, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 25, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 43, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 35, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 24, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 49, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 20, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 20, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 11, clue_position=(0, 6, 1))

    return puzzle
