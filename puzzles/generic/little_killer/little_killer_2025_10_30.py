"""PuzzleMadness Little Killer Sudoku — 2025-10-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 0, 4],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 6, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 2, 0, 0, 0],
        [4, 3, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 34, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 11, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 13, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 43, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 27, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 15, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 34, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 37, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 19, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 19, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 43, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 26, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 44, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 16, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 14, clue_position=(0, 6, 1))

    return puzzle
