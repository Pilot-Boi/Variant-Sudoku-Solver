"""PuzzleMadness Little Killer Sudoku — 2025-02-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 9, 0, 7, 0, 0, 2],
        [0, 0, 4, 3, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 9, 0, 0, 0],
        [0, 1, 0, 0, 3, 0, 0, 5, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 66, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 33, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 38, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 23, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 24, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 24, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 39, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 32, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 29, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 20, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 29, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 31, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 17, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 36, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 45, clue_position=(1, 9, 0))

    return puzzle
