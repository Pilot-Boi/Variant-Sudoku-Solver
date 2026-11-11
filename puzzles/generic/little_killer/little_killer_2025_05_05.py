"""PuzzleMadness Little Killer Sudoku — 2025-05-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [5, 0, 4, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 4, 0],
        [0, 8, 0, 9, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 1, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 19, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 10, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 17, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 14, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 9, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 47, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 42, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 27, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 11, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 14, clue_position=(0, 5, 2))

    return puzzle
