"""PuzzleMadness Little Killer Sudoku — 2025-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [3, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 9, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 8, 0, 5, 0, 0, 4, 0],
        [0, 4, 0, 9, 0, 0, 3, 1, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 27, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 39, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 36, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 5, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 29, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 38, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 28, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 31, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 15, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 24, clue_position=(1, 5, 3))

    return puzzle
