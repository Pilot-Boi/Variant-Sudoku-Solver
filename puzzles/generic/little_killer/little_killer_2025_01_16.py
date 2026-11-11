"""PuzzleMadness Little Killer Sudoku — 2025-01-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 4, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 3, 5, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 9, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 34, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 1), (7, 0)], 10, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 3, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 9, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 28, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 17, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 35, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 20, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 33, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 39, clue_position=(1, 8, 2))

    return puzzle
