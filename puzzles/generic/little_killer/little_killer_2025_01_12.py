"""PuzzleMadness Little Killer Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 4, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 9, 0, 7],
        [0, 6, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 4, 8, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 20, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 23, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 46, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 12, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 42, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 34, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 29, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 13, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 27, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 48, clue_position=(0, -1, 2))

    return puzzle
