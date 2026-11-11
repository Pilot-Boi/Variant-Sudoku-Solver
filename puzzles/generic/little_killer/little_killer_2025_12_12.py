"""PuzzleMadness Little Killer Sudoku — 2025-12-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 9, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 9, 0, 4, 3, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 2, 0, 0, 0, 0, 7, 8, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 4, 0, 0],
        [0, 0, 0, 8, 6, 5, 0, 0, 0],
        [0, 0, 5, 0, 0, 7, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 38, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 20, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 45, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 37, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 22, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 45, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 20, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 33, clue_position=(0, 2, 0))

    return puzzle
