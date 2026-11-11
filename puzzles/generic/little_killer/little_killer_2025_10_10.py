"""PuzzleMadness Little Killer Sudoku — 2025-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [1, 0, 0, 0, 0, 0, 2, 9, 4],
        [2, 0, 5, 0, 0, 6, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 37, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 51, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(8, 1), (7, 0)], 9, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 21, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 23, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 22, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 14, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 20, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 20, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 23, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 32, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 27, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 30, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 39, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 40, clue_position=(0, -1, 0))

    return puzzle
