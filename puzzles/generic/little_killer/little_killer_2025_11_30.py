"""PuzzleMadness Little Killer Sudoku — 2025-11-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 0, 0, 0],
        [0, 9, 0, 4, 0, 0, 0, 0, 0],
        [0, 5, 0, 8, 7, 0, 3, 4, 0],
        [0, 0, 0, 0, 0, 3, 0, 6, 0],
        [4, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 32, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 20, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 32, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 59, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 12, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 8, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 22, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 26, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 41, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 26, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 50, clue_position=(0, 0, 3))

    return puzzle
