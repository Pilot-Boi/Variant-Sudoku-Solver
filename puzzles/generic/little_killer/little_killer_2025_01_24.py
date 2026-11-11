"""PuzzleMadness Little Killer Sudoku — 2025-01-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 3, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [7, 0, 5, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 2, 7, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 5],
        [5, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 22, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 31, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 17, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 23, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 39, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 18, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 35, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 4, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 31, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 29, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 15, clue_position=(0, 6, 3))

    return puzzle
