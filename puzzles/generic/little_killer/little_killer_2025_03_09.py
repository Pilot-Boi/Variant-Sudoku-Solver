"""PuzzleMadness Little Killer Sudoku — 2025-03-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 9, 0],
        [0, 7, 0, 9, 5, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 7, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 6, 0, 8, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 49, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 33, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 14, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 15, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 25, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 22, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 11, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 37, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 22, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 27, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 52, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 32, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 19, clue_position=(1, 4, 1))

    return puzzle
