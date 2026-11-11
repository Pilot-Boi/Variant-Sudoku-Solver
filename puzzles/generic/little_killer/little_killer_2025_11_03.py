"""PuzzleMadness Little Killer Sudoku — 2025-11-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [6, 0, 0, 0, 0, 1, 7, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 1, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 6, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 29, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 27, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 23, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 44, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 43, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 6, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 17, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 46, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 19, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 18, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 38, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 14, clue_position=(1, 5, 0))

    return puzzle
