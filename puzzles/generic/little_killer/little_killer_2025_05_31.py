"""PuzzleMadness Little Killer Sudoku — 2025-05-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 1, 5, 0, 0, 0],
        [8, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 1, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 2, 0, 0, 0, 0, 9, 0, 3],
        [0, 0, 0, 0, 8, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 13, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 18, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 51, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 29, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 16, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 27, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 20, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 12, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 38, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 1), (7, 0)], 11, clue_position=(1, 2, 2))

    return puzzle
