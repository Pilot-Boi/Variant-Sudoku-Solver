"""PuzzleMadness Little Killer Sudoku — 2025-03-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 7, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 4, 6, 0],
        [4, 0, 0, 0, 0, 9, 0, 3, 0],
        [0, 0, 0, 2, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 26, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 20, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 17, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 11, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 41, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 32, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 46, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 8, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 41, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 27, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 26, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 15, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 9, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 36, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 12, clue_position=(1, 2, 3))

    return puzzle
