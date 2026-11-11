"""PuzzleMadness Little Killer Sudoku — 2025-11-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 6, 0, 0],
        [0, 1, 0, 0, 0, 0, 8, 5, 9],
        [0, 0, 0, 0, 0, 2, 7, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [2, 0, 0, 4, 0, 9, 0, 0, 0],
        [0, 0, 6, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 46, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 32, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(1, 0), (0, 1)], 16, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 22, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 17, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 8, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 29, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 40, clue_position=(1, 6, 1))

    return puzzle
