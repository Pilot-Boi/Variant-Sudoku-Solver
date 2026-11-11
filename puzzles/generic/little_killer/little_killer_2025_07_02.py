"""PuzzleMadness Little Killer Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [3, 0, 8, 9, 5, 0, 0, 0, 0],
        [0, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 5, 0],
        [1, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 30, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(8, 1), (7, 0)], 7, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 16, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 18, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 25, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 1), (1, 0)], 13, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 25, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 26, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 40, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 28, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 37, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 50, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 13, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 47, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 43, clue_position=(1, 7, 2))

    return puzzle
