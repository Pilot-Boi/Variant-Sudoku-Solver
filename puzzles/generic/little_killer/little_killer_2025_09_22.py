"""PuzzleMadness Little Killer Sudoku — 2025-09-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 9, 2],
        [0, 2, 0, 7, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 5],
        [0, 0, 5, 0, 0, 2, 0, 0, 0],
        [0, 0, 8, 0, 0, 5, 0, 0, 0],
        [0, 0, 9, 0, 0, 7, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 30, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 13, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 41, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 27, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 26, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(7, 8), (8, 7)], 10, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 19, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 47, clue_position=(0, 0, 0))

    return puzzle
