"""PuzzleMadness Little Killer Sudoku — 2025-10-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [1, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 4, 0, 2, 0, 3, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 4, 6, 7, 0],
        [0, 0, 5, 6, 1, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 16, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 25, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 43, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 23, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 34, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 14, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 38, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 43, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 37, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 18, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 34, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 10, clue_position=(1, 3, 1))

    return puzzle
