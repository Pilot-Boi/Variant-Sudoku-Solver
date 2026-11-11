"""PuzzleMadness Little Killer Sudoku — 2025-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 1, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 6],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 35, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 45, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 25, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 43, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 16, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 30, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 30, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 12, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 18, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 17, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 16, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 22, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 44, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 11, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 12, clue_position=(1, 2, 3))

    return puzzle
