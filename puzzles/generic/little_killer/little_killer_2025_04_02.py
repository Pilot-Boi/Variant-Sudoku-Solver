"""PuzzleMadness Little Killer Sudoku — 2025-04-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 9, 0, 8, 0],
        [0, 0, 4, 0, 5, 0, 0, 0, 0],
        [8, 0, 9, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 9, 4, 0, 1, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 8), (0, 7)], 16, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 46, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 14, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 18, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 31, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 50, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 42, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 17, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 49, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 25, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 22, clue_position=(1, 3, 3))

    return puzzle
