"""PuzzleMadness Little Killer Sudoku — 2025-05-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 4],
        [0, 0, 0, 9, 8, 0, 0, 0, 0],
        [7, 0, 0, 5, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 9, 7, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 21, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 14, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 18, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 13, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 23, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 33, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 35, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 40, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 22, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 34, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 15, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 40, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 8, clue_position=(0, 6, 0))

    return puzzle
