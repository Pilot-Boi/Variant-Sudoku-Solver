"""PuzzleMadness Little Killer Sudoku — 2025-06-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 8, 1, 0, 2, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 3, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 7, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 22, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 30, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 23, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 36, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 36, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 13, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 44, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 11, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 23, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 24, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 1), (7, 0)], 8, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 9, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 6, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 29, clue_position=(1, 8, 2))

    return puzzle
