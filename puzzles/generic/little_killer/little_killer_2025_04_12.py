"""PuzzleMadness Little Killer Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 3, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 4, 3],
        [0, 1, 2, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 52, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 12, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 28, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 19, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 37, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 22, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 33, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 45, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 22, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 17, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 37, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 44, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 38, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 5, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 32, clue_position=(1, 7, 3))

    return puzzle
