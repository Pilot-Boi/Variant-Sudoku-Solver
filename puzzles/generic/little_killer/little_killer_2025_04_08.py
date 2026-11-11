"""PuzzleMadness Little Killer Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 5, 0],
        [0, 0, 0, 6, 0, 0, 2, 0, 0],
        [0, 0, 0, 4, 3, 2, 0, 0, 0],
        [0, 0, 3, 7, 0, 0, 9, 0, 6],
        [1, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 7, 1, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 44, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 12, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 35, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 32, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 7, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 18, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 43, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 49, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 29, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(1, 8), (0, 7)], 3, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 36, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 28, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 24, clue_position=(1, 4, 0))

    return puzzle
