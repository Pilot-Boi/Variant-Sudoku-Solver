"""PuzzleMadness Little Killer Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 7, 3, 0, 0, 0, 0, 0, 5],
        [0, 5, 6, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 8, 0, 4, 0, 0, 0, 1],
        [3, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 9, 5, 0, 0, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 22, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 17, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 31, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 13, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 22, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 11, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 26, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 44, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 53, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 32, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 49, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 31, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 40, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 10, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 16, clue_position=(1, 7, 1))

    return puzzle
