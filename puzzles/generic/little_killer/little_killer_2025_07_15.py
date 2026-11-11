"""PuzzleMadness Little Killer Sudoku — 2025-07-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 6],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 3, 0, 5, 8],
        [0, 0, 0, 0, 9, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 18, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 7), (1, 8)], 5, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 22, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 22, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 41, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 34, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 26, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 49, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 17, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(7, 0), (8, 1)], 7, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 8, clue_position=(1, 4, 2))

    return puzzle
