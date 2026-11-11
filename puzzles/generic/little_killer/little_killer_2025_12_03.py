"""PuzzleMadness Little Killer Sudoku — 2025-12-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 7, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 6, 1, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 6, 7, 2, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 40, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 39, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 26, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 13, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 29, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 12, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 18, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 46, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 15, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 27, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 38, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 21, clue_position=(1, 4, 3))

    return puzzle
