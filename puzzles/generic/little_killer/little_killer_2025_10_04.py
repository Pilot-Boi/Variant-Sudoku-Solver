"""PuzzleMadness Little Killer Sudoku — 2025-10-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 5, 6, 0, 0, 0, 9],
        [6, 0, 0, 0, 0, 7, 0, 4, 1],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 7, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 15, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 36, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 40, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 45, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 15, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 19, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 22, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 31, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 24, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 49, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 23, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 47, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 20, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 15, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 11, clue_position=(1, 2, 0))

    return puzzle
