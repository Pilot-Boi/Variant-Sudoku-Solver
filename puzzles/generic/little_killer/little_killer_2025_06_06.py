"""PuzzleMadness Little Killer Sudoku — 2025-06-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 5, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 8, 4, 0, 0],
        [0, 0, 8, 0, 1, 0, 0, 0, 0],
        [9, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 5],
        [0, 0, 0, 9, 4, 1, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 32, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 35, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 26, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 15, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 44, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 9, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 45, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 23, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 38, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 46, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 4, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 30, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 23, clue_position=(0, 4, 3))

    return puzzle
