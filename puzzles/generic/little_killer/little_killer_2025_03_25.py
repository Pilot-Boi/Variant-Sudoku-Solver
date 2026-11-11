"""PuzzleMadness Little Killer Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 2, 0, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 0, 0, 4],
        [5, 0, 0, 3, 0, 0, 0, 7, 0],
        [0, 0, 0, 6, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 5, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [1, 0, 5, 4, 3, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 0), (8, 1)], 13, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 33, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 33, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 46, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 28, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 25, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 46, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 24, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 18, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 31, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 6, clue_position=(1, 4, 3))

    return puzzle
