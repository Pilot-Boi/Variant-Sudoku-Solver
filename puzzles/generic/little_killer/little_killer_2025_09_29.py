"""PuzzleMadness Little Killer Sudoku — 2025-09-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 8],
        [0, 0, 0, 0, 0, 8, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 9, 0],
        [0, 0, 6, 0, 7, 0, 4, 0, 0],
        [0, 0, 3, 0, 6, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 39, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 11, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 39, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 14, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 47, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 14, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 41, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 11, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 27, clue_position=(1, 6, 3))

    return puzzle
