"""PuzzleMadness Little Killer Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 2, 3, 0, 0, 0, 0, 0, 0],
        [1, 6, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [8, 0, 0, 1, 0, 0, 6, 5, 4],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 7, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 44, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 36, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 12, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 22, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 26, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 17, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(1, 8), (0, 7)], 10, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 33, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 20, clue_position=(0, 5, 3))

    return puzzle
