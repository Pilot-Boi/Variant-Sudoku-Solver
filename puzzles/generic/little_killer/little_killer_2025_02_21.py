"""PuzzleMadness Little Killer Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 0, 0, 9, 4],
        [0, 0, 2, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 9, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 33, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 19, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 19, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 17, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 55, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 23, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 41, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 1), (1, 0)], 7, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 36, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 25, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 21, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 33, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 4, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 25, clue_position=(1, 5, 1))

    return puzzle
