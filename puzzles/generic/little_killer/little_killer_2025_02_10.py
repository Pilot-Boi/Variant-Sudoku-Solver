"""PuzzleMadness Little Killer Sudoku — 2025-02-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-02-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/2/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0, 0, 0],
        [1, 4, 7, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 2, 9, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 24, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 27, clue_position=(1, 5, 3))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 25, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 46, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 41, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 38, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 40, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 24, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 13, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 1), (7, 2), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)], 37, clue_position=(0, 0, 2))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 22, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(6, 8), (7, 7), (8, 6)], 10, clue_position=(0, 5, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 36, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 42, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 17, clue_position=(1, 4, 2))

    return puzzle
