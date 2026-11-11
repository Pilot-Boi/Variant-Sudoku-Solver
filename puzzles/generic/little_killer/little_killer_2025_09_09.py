"""PuzzleMadness Little Killer Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 6],
        [0, 0, 0, 5, 0, 0, 1, 0, 3],
        [7, 9, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 7, 3, 0, 0],
        [0, 1, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 3, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 15, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 15, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 33, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(7, 8), (8, 7)], 10, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 38, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 43, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 20, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 28, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 20, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 28, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 36, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 26, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 24, clue_position=(0, 3, 0))

    return puzzle
