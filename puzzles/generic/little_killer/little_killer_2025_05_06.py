"""PuzzleMadness Little Killer Sudoku — 2025-05-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 5, 0, 0],
        [0, 6, 0, 0, 9, 0, 1, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 4, 3, 0, 0, 9, 0, 7, 0],
        [0, 0, 0, 0, 6, 1, 0, 4, 0],
        [6, 1, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 17, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 46, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 33, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 17, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 29, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 15, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 43, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 8, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 24, clue_position=(1, 6, 1))

    return puzzle
