"""PuzzleMadness Little Killer Sudoku — 2025-04-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-04-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/4/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 2],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 4, 1, 0, 0, 0, 0, 0, 9],
        [0, 0, 8, 0, 0, 4, 0, 0, 0],
        [3, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 3],
        [0, 0, 6, 0, 3, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 17, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 31, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 49, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 20, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 8, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 18, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 46, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 18, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 12, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 21, clue_position=(0, 3, 3))

    return puzzle
