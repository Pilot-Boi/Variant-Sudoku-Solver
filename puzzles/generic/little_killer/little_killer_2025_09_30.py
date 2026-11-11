"""PuzzleMadness Little Killer Sudoku — 2025-09-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 2, 0, 0, 0],
        [0, 3, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 25, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 13, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 3, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 15, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 9, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 43, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 25, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 1), (1, 0)], 17, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 55, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 31, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 29, clue_position=(0, 1, 3))

    return puzzle
