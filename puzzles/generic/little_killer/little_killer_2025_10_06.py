"""PuzzleMadness Little Killer Sudoku — 2025-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 9, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 7, 5, 2, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 6, 7],
        [0, 0, 0, 9, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [9, 0, 0, 2, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 20, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 19, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 22, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 35, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 45, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 14, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 25, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 13, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 42, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 19, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 32, clue_position=(0, 2, 3))

    return puzzle
