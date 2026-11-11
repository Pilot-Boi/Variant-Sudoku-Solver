"""PuzzleMadness Little Killer Sudoku — 2025-06-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 5, 9],
        [0, 0, 0, 0, 0, 2, 0, 7, 0],
        [0, 6, 0, 0, 4, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 5, 8, 0],
        [4, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 25, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 26, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 37, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 4, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 31, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 31, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 38, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 20, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 21, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 31, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 54, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 22, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 30, clue_position=(0, 1, 2))

    return puzzle
