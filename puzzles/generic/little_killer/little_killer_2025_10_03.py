"""PuzzleMadness Little Killer Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 6],
        [0, 0, 0, 0, 5, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 4, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 5, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 6, 3, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 29, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 13, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 43, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 6, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 9, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 25, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 48, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 22, clue_position=(0, 1, 2))

    return puzzle
