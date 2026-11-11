"""PuzzleMadness Little Killer Sudoku — 2025-03-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 7, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 9, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 9],
        [0, 8, 0, 0, 0, 1, 0, 9, 0],
        [7, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 9, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 15, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 22, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 10, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 35, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 17, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 43, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 27, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 6, clue_position=(1, 2, 1))

    return puzzle
