"""PuzzleMadness Renban Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 1, 0, 4, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 5, 0, 3, 0, 0, 0, 0],
        [0, 0, 6, 1, 0, 0, 0, 0, 0],
        [0, 1, 8, 4, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 1, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 2), (3, 2), (4, 2), (4, 3), (4, 4)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 5), (6, 6), (7, 7)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(1, 6), (1, 5), (2, 5), (3, 5)])
    puzzle.add_renban([(0, 4), (1, 4), (2, 4), (3, 4)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(0, 1), (1, 1), (2, 1)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(0, 2), (1, 3)])
    puzzle.add_renban([(4, 8), (4, 7)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(2, 7), (2, 6)])
    puzzle.add_renban([(7, 4), (6, 4)])

    return puzzle
