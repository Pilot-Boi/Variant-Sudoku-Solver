"""PuzzleMadness Little Killer Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 5, 8, 0, 0],
        [0, 0, 0, 0, 2, 3, 0, 0, 0],
        [1, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 3, 0, 9],
        [0, 0, 1, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 6, 0, 0],
        [0, 7, 0, 2, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 37, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 23, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 25, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 29, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 41, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 10, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(1, 8), (0, 7)], 8, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 22, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 56, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 22, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 9, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 29, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 36, clue_position=(1, 6, 0))

    return puzzle
