"""PuzzleMadness Little Killer Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 3, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 7, 0],
        [0, 4, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 1, 9, 3, 0, 0, 5, 8],
        [0, 0, 3, 0, 0, 2, 0, 0, 0],
        [0, 3, 0, 5, 0, 8, 0, 6, 0],
        [1, 0, 0, 7, 0, 0, 5, 0, 4],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 17, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 13, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 31, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 43, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 10, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 27, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 31, clue_position=(1, 6, 1))

    return puzzle
