"""PuzzleMadness Little Killer Sudoku — 2025-09-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 5, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 9, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 4],
        [0, 0, 2, 1, 0, 4, 0, 0, 0],
        [8, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 39, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 24, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 9, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 17, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 38, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 20, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 20, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 37, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 22, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 43, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 15, clue_position=(0, 5, 0))

    return puzzle
