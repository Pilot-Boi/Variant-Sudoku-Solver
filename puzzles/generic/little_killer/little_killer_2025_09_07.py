"""PuzzleMadness Little Killer Sudoku — 2025-09-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 4, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 8, 5, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 5, 0, 0, 0],
        [6, 0, 0, 7, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [4, 7, 0, 0, 0, 1, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 49, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 38, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 7), (7, 8)], 17, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 29, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 17, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 21, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 29, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(4, 8), (3, 7), (2, 6), (1, 5), (0, 4)], 30, clue_position=(1, 5, 1))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 47, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 42, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 22, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 12, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 13, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 13, clue_position=(1, 3, 2))

    return puzzle
