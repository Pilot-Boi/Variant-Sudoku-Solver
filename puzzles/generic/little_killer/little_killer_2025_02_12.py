"""PuzzleMadness Little Killer Sudoku — 2025-02-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 7, 0, 0, 9, 0, 0],
        [0, 7, 0, 0, 0, 0, 6, 2, 0],
        [1, 8, 5, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 3, 0, 1, 0, 4, 0],
        [4, 0, 0, 0, 7, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 1, 0, 0, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 35, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 31, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 31, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 22, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 55, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 25, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 12, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 35, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 32, clue_position=(0, 1, 0))

    return puzzle
