"""PuzzleMadness Renban Sudoku — 2025-07-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 7],
        [0, 0, 0, 8, 0, 0, 2, 0, 0],
        [9, 0, 0, 0, 0, 3, 0, 4, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [2, 6, 7, 0, 0, 5, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 1, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 2), (6, 2), (5, 2), (5, 1), (5, 0)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    puzzle.add_renban([(3, 6), (4, 5), (5, 4), (6, 5), (7, 6)])
    puzzle.add_renban([(1, 6), (2, 6), (2, 7), (2, 8)])
    puzzle.add_renban([(1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_renban([(5, 6), (5, 7), (4, 7)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(4, 1), (4, 2), (3, 2)])
    puzzle.add_renban([(3, 3), (4, 3), (5, 3)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(8, 4), (7, 5)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(1, 1), (1, 2)])
    puzzle.add_renban([(8, 7), (7, 7)])

    return puzzle
