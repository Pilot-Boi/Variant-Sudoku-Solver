"""PuzzleMadness Little Killer Sudoku — 2025-05-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 5, 0, 2, 0],
        [3, 0, 6, 0, 0, 0, 8, 1, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 30, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 33, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 15, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 24, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 36, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 27, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 47, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 38, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 13, clue_position=(0, 4, 1))

    return puzzle
