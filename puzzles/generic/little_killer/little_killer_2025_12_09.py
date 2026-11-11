"""PuzzleMadness Little Killer Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 4],
        [0, 0, 8, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 2, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 15, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 41, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 20, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 23, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 31, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 29, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 43, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 7, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 21, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 21, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 25, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 48, clue_position=(0, -1, 0))

    return puzzle
