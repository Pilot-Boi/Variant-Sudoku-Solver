"""PuzzleMadness Little Killer Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 5, 0, 1, 6],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 5, 0, 8, 0, 7, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 9, 0, 2, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 26, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 28, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 22, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 23, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 10, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 17, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 39, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 1), (1, 0)], 13, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 42, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 17, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 43, clue_position=(0, 1, 1))

    return puzzle
