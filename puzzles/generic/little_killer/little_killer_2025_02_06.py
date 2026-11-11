"""PuzzleMadness Little Killer Sudoku — 2025-02-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 9, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [9, 4, 2, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 6, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 27, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 18, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 24, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 19, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 20, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(7, 8), (8, 7)], 7, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 13, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 17, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 44, clue_position=(0, -1, 2))

    return puzzle
