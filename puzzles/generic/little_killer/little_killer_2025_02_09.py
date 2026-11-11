"""PuzzleMadness Little Killer Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 6, 7, 0, 0, 0],
        [9, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 9, 0],
        [0, 7, 2, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 34, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 38, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 39, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 18, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 23, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 15, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 21, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 44, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 7), (7, 8)], 17, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 19, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 38, clue_position=(0, 0, 2))

    return puzzle
