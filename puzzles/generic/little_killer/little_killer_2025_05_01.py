"""PuzzleMadness Little Killer Sudoku — 2025-05-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 7],
        [0, 6, 0, 7, 0, 0, 0, 9, 0],
        [8, 0, 1, 0, 6, 3, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 0), (0, 1)], 7, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 5, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 33, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 25, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 26, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 14, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 21, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 20, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 29, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 40, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 15, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 12, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 29, clue_position=(1, 6, 3))

    return puzzle
