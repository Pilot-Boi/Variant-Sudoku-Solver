"""PuzzleMadness Little Killer Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 9, 0, 6, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 4, 0, 0, 6],
        [0, 0, 0, 2, 6, 9, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 9],
        [8, 0, 0, 6, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 44, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 48, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 25, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 19, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 28, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 35, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 24, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 14, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 19, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 20, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 38, clue_position=(1, 8, 3))

    return puzzle
