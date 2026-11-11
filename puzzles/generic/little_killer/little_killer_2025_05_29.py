"""PuzzleMadness Little Killer Sudoku — 2025-05-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 7, 0, 5, 0, 0],
        [0, 8, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 2, 0, 0, 9, 0, 0, 0],
        [0, 0, 8, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 22, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 27, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 4, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(3, 0), (4, 1), (5, 2), (6, 3), (7, 4), (8, 5)], 30, clue_position=(0, 2, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 31, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(0, 7), (1, 8)], 4, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 45, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 24, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 17, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 31, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 15, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 11, clue_position=(0, 6, 3))

    return puzzle
