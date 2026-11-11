"""PuzzleMadness Little Killer Sudoku — 2025-04-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 7, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 3, 4, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 9, 6],
        [0, 0, 0, 7, 0, 5, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 20, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 43, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 51, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 8, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 28, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 48, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 22, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 15, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 30, clue_position=(1, 6, 1))

    return puzzle
