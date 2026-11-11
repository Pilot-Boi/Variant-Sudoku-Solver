"""PuzzleMadness Little Killer Sudoku — 2025-08-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 2, 0, 0, 6],
        [0, 6, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 3],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 8, 3, 0, 0, 0, 4],
        [5, 9, 0, 0, 0, 0, 0, 0, 8],
        [6, 0, 0, 1, 0, 0, 0, 5, 0],
        [0, 3, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 27, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 17, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 28, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 21, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 32, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 36, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 15, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 41, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 13, clue_position=(1, 2, 3))

    return puzzle
