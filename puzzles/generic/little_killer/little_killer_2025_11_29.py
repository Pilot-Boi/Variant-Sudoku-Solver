"""PuzzleMadness Little Killer Sudoku — 2025-11-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [3, 0, 0, 0, 7, 0, 0, 2, 0],
        [0, 0, 0, 0, 3, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 8, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 44, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 28, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 18, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 13, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 48, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 7), (1, 8)], 7, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 27, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 31, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 9, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 19, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 30, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 16, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 46, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 32, clue_position=(1, 7, 0))

    return puzzle
