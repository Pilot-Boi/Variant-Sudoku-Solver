"""PuzzleMadness Little Killer Sudoku — 2025-09-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 4, 0, 0, 1, 7, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 9, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 50, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 32, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 15, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 31, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 40, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 10, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 0), (8, 1)], 17, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 12, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 12, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 50, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 17, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 7, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 16, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 10, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 15, clue_position=(0, 3, 3))

    return puzzle
