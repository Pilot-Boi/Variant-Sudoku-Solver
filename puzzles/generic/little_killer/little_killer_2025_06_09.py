"""PuzzleMadness Little Killer Sudoku — 2025-06-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 9, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 4],
        [7, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 1, 5, 0, 7, 9],
        [0, 0, 0, 0, 0, 0, 0, 4, 3],
        [0, 0, 9, 0, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 47, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 11, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 49, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 41, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 14, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 33, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 20, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 26, clue_position=(0, 3, 3))

    return puzzle
