"""PuzzleMadness Little Killer Sudoku — 2025-08-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 7, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 9, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 5, 0, 6, 3],
        [0, 0, 0, 9, 3, 0, 0, 0, 0],
        [9, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 25, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 26, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 41, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 26, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 11, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 28, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 8, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 36, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 19, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 32, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 35, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 21, clue_position=(1, 4, 1))

    return puzzle
