"""PuzzleMadness Little Killer Sudoku — 2025-12-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 3, 0, 0, 0, 0, 6, 7],
        [5, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 6, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 6, 0, 2, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [7, 0, 0, 0, 0, 3, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 38, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 13, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 39, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 15, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 22, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 28, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 31, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 44, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 14, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(1, 8), (0, 7)], 4, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 46, clue_position=(0, -1, 0))

    return puzzle
