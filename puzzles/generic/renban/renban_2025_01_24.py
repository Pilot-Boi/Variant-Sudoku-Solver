"""PuzzleMadness Renban Sudoku — 2025-01-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 7, 0, 6],
        [1, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 2, 0, 9, 0, 0, 0, 0, 8],
        [0, 0, 0, 2, 0, 6, 9, 0, 0],
        [8, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 5],
        [0, 0, 0, 0, 0, 2, 4, 0, 0],
        [0, 0, 0, 1, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 0), (6, 1), (5, 2), (4, 1), (3, 0)])
    puzzle.add_renban([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(6, 6), (5, 7), (4, 8), (3, 7), (2, 6)])
    puzzle.add_renban([(3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(8, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (2, 1)])
    puzzle.add_renban([(4, 7), (4, 6), (5, 6)])
    puzzle.add_renban([(3, 1), (4, 2), (5, 3)])
    puzzle.add_renban([(8, 5), (7, 5)])
    puzzle.add_renban([(8, 8), (7, 7)])
    puzzle.add_renban([(6, 5), (5, 5)])
    puzzle.add_renban([(2, 2), (3, 2)])
    puzzle.add_renban([(7, 8), (6, 7)])

    return puzzle
