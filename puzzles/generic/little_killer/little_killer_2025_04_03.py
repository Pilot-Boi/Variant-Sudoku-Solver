"""PuzzleMadness Little Killer Sudoku — 2025-04-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 8, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 3, 0, 6, 7, 0],
        [1, 0, 5, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [9, 0, 0, 0, 6, 0, 0, 1, 0],
        [0, 0, 0, 0, 7, 0, 0, 8, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 32, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 47, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 1), (1, 0)], 9, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 41, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 9, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 38, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 8, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 26, clue_position=(1, 6, 0))

    return puzzle
