"""PuzzleMadness Little Killer Sudoku — 2025-12-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 7, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 5, 6],
        [0, 0, 6, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 33, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 12, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 39, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 11, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 21, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 10, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 14, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 29, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 18, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 38, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 19, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 5, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 22, clue_position=(0, 3, 3))

    return puzzle
