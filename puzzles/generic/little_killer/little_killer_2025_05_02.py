"""PuzzleMadness Little Killer Sudoku — 2025-05-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 3, 6, 9, 0, 0, 2],
        [8, 0, 6, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 9, 0, 5, 0, 4, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 17, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 17, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 40, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 7, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 16, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 42, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 32, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 34, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 42, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 9, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 38, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 38, clue_position=(0, 1, 3))

    return puzzle
