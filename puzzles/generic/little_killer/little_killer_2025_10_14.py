"""PuzzleMadness Little Killer Sudoku — 2025-10-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 0, 2, 0],
        [0, 0, 5, 0, 6, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 8, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 2, 0, 3, 0],
        [0, 0, 3, 0, 0, 7, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 51, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 47, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 21, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 20, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 30, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 19, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 45, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 44, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 30, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 23, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 30, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 16, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 35, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 22, clue_position=(0, 4, 3))

    return puzzle
