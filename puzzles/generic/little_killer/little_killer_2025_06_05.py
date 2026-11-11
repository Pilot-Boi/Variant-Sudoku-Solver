"""PuzzleMadness Little Killer Sudoku — 2025-06-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 2, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 7, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 0],
        [7, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 8, 0, 2, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 32, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 20, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 17, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 22, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 32, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 31, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(7, 8), (8, 7)], 10, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 16, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 9, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 1), (1, 0)], 5, clue_position=(1, 2, 0))

    return puzzle
