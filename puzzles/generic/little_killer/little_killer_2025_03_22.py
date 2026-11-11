"""PuzzleMadness Little Killer Sudoku — 2025-03-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 4, 0, 8, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 7, 0, 0, 9, 8],
        [0, 0, 2, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 30, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 13, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 26, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 33, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 32, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 18, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 26, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 7, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 22, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 8, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 27, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 43, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 29, clue_position=(0, 3, 2))

    return puzzle
