"""PuzzleMadness Little Killer Sudoku — 2025-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 7, 0, 2, 0, 8],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 6, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 31, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 32, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 18, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 33, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 8, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 14, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 19, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 41, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 9, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 32, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 31, clue_position=(0, 2, 1))

    return puzzle
