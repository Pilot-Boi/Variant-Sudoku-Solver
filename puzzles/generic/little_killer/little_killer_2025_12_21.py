"""PuzzleMadness Little Killer Sudoku — 2025-12-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 4, 0, 0, 5, 0, 7, 0, 9],
        [0, 0, 1, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [7, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 2, 0, 5],
        [0, 3, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 20, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 15, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 9, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 30, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 7, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 25, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 35, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 46, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 18, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 41, clue_position=(1, 9, 0))

    return puzzle
