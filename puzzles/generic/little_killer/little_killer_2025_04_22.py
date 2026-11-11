"""PuzzleMadness Little Killer Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 2, 0, 0, 8, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 7],
        [0, 5, 0, 0, 6, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 5, 0, 0, 7, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 15, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 27, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 33, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 15, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(1, 8), (0, 7)], 7, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 17, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 28, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 26, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 30, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 30, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 34, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 39, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 27, clue_position=(0, 3, 1))

    return puzzle
