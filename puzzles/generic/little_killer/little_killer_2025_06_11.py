"""PuzzleMadness Little Killer Sudoku — 2025-06-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 5, 0, 3],
        [0, 0, 0, 8, 0, 0, 0, 2, 0],
        [0, 9, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 7, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 25, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 16, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(7, 8), (8, 7)], 3, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 25, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 13, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 34, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 35, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 12, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 13, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 25, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 46, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 21, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 49, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 39, clue_position=(1, 7, 2))

    return puzzle
