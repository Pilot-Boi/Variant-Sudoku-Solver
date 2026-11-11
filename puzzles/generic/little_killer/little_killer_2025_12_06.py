"""PuzzleMadness Little Killer Sudoku — 2025-12-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
        [5, 4, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 5, 1, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (0, 7)], 5, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 15, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 49, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 39, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 15, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 21, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 35, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 12, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 30, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 17, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 28, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 34, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 26, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))

    return puzzle
