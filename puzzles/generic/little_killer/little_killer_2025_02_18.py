"""PuzzleMadness Little Killer Sudoku — 2025-02-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 5, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 4],
        [0, 0, 0, 0, 0, 2, 8, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 7, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 0), (0, 1)], 4, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 49, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(8, 1), (7, 0)], 17, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 7, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 12, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 26, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 29, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 20, clue_position=(0, 5, 2))

    return puzzle
