"""PuzzleMadness Little Killer Sudoku — 2025-10-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 3, 0, 0, 0, 5, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 8, 9, 0, 0],
        [9, 0, 0, 0, 0, 0, 2, 6, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 13, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 23, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 47, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 43, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 24, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 38, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 12, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 32, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 13, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 22, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 32, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 36, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 8, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 35, clue_position=(1, 7, 3))

    return puzzle
