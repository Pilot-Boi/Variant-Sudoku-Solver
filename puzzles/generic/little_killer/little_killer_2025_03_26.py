"""PuzzleMadness Little Killer Sudoku — 2025-03-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 3, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 6],
        [1, 0, 0, 0, 0, 3, 0, 2, 4],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 6, 9, 8, 0, 0, 0, 0],
        [0, 4, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 28, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 16, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 36, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 40, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 21, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 26, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 47, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 32, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 21, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 24, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 28, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 1), (7, 0)], 12, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 40, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 22, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 44, clue_position=(0, 0, 3))

    return puzzle
