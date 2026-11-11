"""PuzzleMadness Little Killer Sudoku — 2025-04-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 1, 0],
        [0, 0, 0, 5, 0, 0, 9, 7, 0],
        [0, 0, 6, 2, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 8, 2, 1, 3, 0],
        [5, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 23, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 15, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 10, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 21, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 35, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 15, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 39, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 9, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 14, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 53, clue_position=(1, 9, 0))

    return puzzle
