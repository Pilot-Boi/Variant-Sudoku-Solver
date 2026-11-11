"""PuzzleMadness Little Killer Sudoku — 2025-03-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 2, 0, 0],
        [0, 0, 7, 0, 0, 6, 0, 5, 0],
        [5, 0, 6, 0, 0, 3, 8, 1, 0],
        [0, 0, 5, 6, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 36, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 31, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 11, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 16, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 34, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 29, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 11, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 27, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 11, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 27, clue_position=(1, 6, 3))

    return puzzle
