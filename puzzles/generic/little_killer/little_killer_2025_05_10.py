"""PuzzleMadness Little Killer Sudoku — 2025-05-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 3, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [3, 0, 0, 0, 0, 8, 0, 0, 6],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 5, 2, 0, 0, 0],
        [0, 0, 4, 0, 6, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [8, 0, 9, 0, 2, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 23, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 24, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 16, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 19, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 21, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 35, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 37, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 25, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 10, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 33, clue_position=(1, 6, 2))

    return puzzle
