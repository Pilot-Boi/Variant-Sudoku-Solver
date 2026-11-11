"""PuzzleMadness Little Killer Sudoku — 2025-06-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 5, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 8, 0, 6],
        [0, 0, 5, 8, 0, 4, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 4, 0, 6, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 22, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 28, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 52, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 37, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 32, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(7, 0), (8, 1)], 11, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 23, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 13, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 8, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 44, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 28, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 43, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 41, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 20, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 36, clue_position=(0, 2, 0))

    return puzzle
