"""PuzzleMadness Little Killer Sudoku — 2025-06-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 3, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 6],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [6, 0, 7, 0, 0, 5, 0, 0, 9],
        [1, 4, 0, 0, 3, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 21, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 15, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 54, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 11, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 23, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 27, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 19, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 1), (1, 0)], 11, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 27, clue_position=(0, 3, 2))

    return puzzle
