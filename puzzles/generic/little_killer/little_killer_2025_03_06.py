"""PuzzleMadness Little Killer Sudoku — 2025-03-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 4, 0, 0, 0, 6, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 5, 4, 2],
        [0, 0, 0, 0, 0, 2, 0, 0, 9],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 22, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 9, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 4, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 45, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 21, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 12, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 14, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 33, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 23, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 1), (7, 0)], 17, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 49, clue_position=(0, 0, 2))

    return puzzle
