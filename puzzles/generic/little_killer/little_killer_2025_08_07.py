"""PuzzleMadness Little Killer Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [3, 5, 0, 0, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 7, 4, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 9, 0],
        [0, 4, 6, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 37, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 1), (7, 0)], 13, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 40, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 36, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 47, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 35, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 8, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 17, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 14, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 23, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(7, 8), (8, 7)], 8, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 26, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 12, clue_position=(0, 5, 3))

    return puzzle
