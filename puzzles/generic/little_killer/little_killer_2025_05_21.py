"""PuzzleMadness Little Killer Sudoku — 2025-05-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 2, 3],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 6, 0, 3, 9, 0],
        [0, 0, 0, 1, 0, 0, 8, 0, 0],
        [0, 0, 9, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 17, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 41, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 37, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 16, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 33, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 11, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 29, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 38, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 14, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 38, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 25, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 1), (1, 0)], 15, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 47, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 18, clue_position=(0, 4, 0))

    return puzzle
