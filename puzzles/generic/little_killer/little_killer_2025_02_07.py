"""PuzzleMadness Little Killer Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [5, 0, 0, 7, 6, 0, 0, 4, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 0, 0, 3, 0, 8],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [2, 6, 0, 1, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [8, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 37, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 27, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 14, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 38, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 18, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 21, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 34, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 35, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 19, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 43, clue_position=(0, -1, 0))

    return puzzle
