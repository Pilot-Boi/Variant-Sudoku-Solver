"""PuzzleMadness Little Killer Sudoku — 2025-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 9, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 2, 8, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 4, 0, 8, 0, 1, 0],
        [1, 0, 0, 8, 0, 6, 0, 0, 7],
        [4, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 8, 0, 0, 5, 7, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 25, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 13, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 38, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 33, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 19, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 28, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 26, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 16, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 45, clue_position=(1, 8, 1))

    return puzzle
