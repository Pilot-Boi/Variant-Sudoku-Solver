"""PuzzleMadness Renban Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 6, 0, 5, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 8, 0, 0, 0, 2, 7, 0, 0],
        [4, 9, 0, 0, 0, 0, 0, 1, 8],
        [8, 0, 0, 0, 5, 0, 0, 7, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 2, 9, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 6), (2, 5), (2, 4), (3, 4), (4, 4)])
    puzzle.add_renban([(8, 6), (8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8), (4, 8), (5, 8)])
    puzzle.add_renban([(3, 7), (3, 6), (3, 5), (4, 5)])
    puzzle.add_renban([(7, 5), (6, 5), (6, 4), (6, 3)])
    puzzle.add_renban([(6, 2), (6, 1), (7, 1), (8, 1)])
    puzzle.add_renban([(2, 7), (1, 7), (1, 6)])
    puzzle.add_renban([(7, 6), (7, 7), (6, 7)])
    puzzle.add_renban([(7, 2), (8, 2), (8, 3)])
    puzzle.add_renban([(1, 0), (2, 1), (3, 2)])
    puzzle.add_renban([(4, 1), (5, 1)])
    puzzle.add_renban([(8, 4), (7, 4)])
    puzzle.add_renban([(0, 8), (0, 7)])
    puzzle.add_renban([(1, 1), (1, 2)])
    puzzle.add_renban([(5, 7), (5, 6)])

    return puzzle
