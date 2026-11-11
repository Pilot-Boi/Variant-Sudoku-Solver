"""PuzzleMadness Little Killer Sudoku — 2025-06-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 5, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 3, 2, 0, 7],
        [0, 0, 0, 8, 0, 1, 9, 0, 0],
        [0, 0, 0, 0, 5, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 8), (8, 7)], 11, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 10, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 49, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 18, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 13, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 46, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 37, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 18, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 20, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 35, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 25, clue_position=(1, 5, 1))

    return puzzle
