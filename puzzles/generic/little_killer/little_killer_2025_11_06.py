"""PuzzleMadness Little Killer Sudoku — 2025-11-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 3, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 6, 0],
        [0, 8, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 7, 0, 0],
        [6, 0, 0, 0, 5, 0, 8, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 9, 7],
        [0, 0, 8, 0, 0, 0, 6, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 41, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 1), (1, 0)], 10, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 14, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 20, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 19, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 48, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 39, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 24, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 39, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 46, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 31, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 38, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 30, clue_position=(1, 8, 0))

    return puzzle
