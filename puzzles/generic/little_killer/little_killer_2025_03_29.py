"""PuzzleMadness Little Killer Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 3, 0, 0, 0, 2, 0, 0, 0],
        [5, 0, 0, 3, 0, 0, 0, 4, 2],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 9, 1, 0, 0, 0, 7],
        [8, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 27, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 42, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(1, 8), (0, 7)], 10, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 35, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 39, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 40, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 49, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 39, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 15, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 18, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 15, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 43, clue_position=(1, 9, 2))

    return puzzle
