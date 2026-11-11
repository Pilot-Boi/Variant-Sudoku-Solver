"""PuzzleMadness Little Killer Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 6, 1, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 0],
        [4, 0, 8, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 8, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 32, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 7, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 7, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 22, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 7, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 19, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 13, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 14, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 31, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 38, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 24, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 21, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 40, clue_position=(0, 0, 3))

    return puzzle
