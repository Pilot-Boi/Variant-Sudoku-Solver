"""PuzzleMadness Little Killer Sudoku — 2025-05-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 5, 8],
        [0, 0, 7, 0, 0, 0, 2, 3, 0],
        [0, 0, 0, 0, 0, 1, 3, 8, 0],
        [4, 1, 5, 3, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 29, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 49, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 45, clue_position=(1, 8, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 27, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 17, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 19, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 5, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 10, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 33, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 38, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 30, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 14, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 22, clue_position=(0, 2, 2))

    return puzzle
