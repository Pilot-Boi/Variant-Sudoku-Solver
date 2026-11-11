"""PuzzleMadness Little Killer Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 1, 4],
        [0, 0, 0, 0, 6, 0, 0, 3, 0],
        [0, 0, 0, 7, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 4, 0, 0, 0, 7],
        [0, 3, 2, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 34, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 8, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 31, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 45, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 16, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 55, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 19, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 32, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 41, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 19, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 18, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 25, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 46, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 40, clue_position=(0, 0, 1))

    return puzzle
