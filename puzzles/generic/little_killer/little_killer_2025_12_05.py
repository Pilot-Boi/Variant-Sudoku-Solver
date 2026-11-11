"""PuzzleMadness Little Killer Sudoku — 2025-12-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 7, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 3, 2],
        [0, 8, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 46, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 39, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 36, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 10, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 12, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 41, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 28, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 15, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 25, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 21, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 27, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 12, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 37, clue_position=(1, 8, 3))

    return puzzle
