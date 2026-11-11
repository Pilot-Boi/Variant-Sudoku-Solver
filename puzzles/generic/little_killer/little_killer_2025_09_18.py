"""PuzzleMadness Little Killer Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 8, 0, 5, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 2, 0, 4, 5, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 8, 4, 0, 0, 9, 7, 0, 0],
        [0, 0, 0, 0, 4, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 0), (8, 1)], 10, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 8, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 22, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 32, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 20, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 43, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 44, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 34, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 15, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 30, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 26, clue_position=(1, 5, 1))

    return puzzle
