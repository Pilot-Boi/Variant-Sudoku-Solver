"""PuzzleMadness Little Killer Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 5, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 9, 0, 0, 7, 0, 2],
        [0, 3, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 29, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 10, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 18, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 30, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 50, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 10, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 43, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 34, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 36, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 13, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 30, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 15, clue_position=(1, 2, 3))

    return puzzle
