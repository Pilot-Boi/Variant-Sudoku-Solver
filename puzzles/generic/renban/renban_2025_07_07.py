"""PuzzleMadness Renban Sudoku — 2025-07-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 8, 0, 0, 4, 2, 0, 3, 5],
        [0, 0, 0, 1, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 8, 4, 0, 0, 0],
        [5, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 5, 0, 0, 0, 8],
        [0, 0, 6, 0, 0, 0, 0, 0, 7],
        [8, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 2), (3, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (4, 6), (4, 7)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_renban([(4, 1), (5, 1), (6, 1), (7, 1)])
    puzzle.add_renban([(8, 5), (7, 6), (6, 7), (5, 6)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(4, 4), (5, 4), (5, 5)])
    puzzle.add_renban([(8, 3), (7, 4), (6, 5)])
    puzzle.add_renban([(0, 5), (0, 4), (1, 4)])
    puzzle.add_renban([(1, 1), (1, 2), (1, 3)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(7, 3), (6, 4)])
    puzzle.add_renban([(3, 4), (4, 3)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(1, 0), (2, 0)])

    return puzzle
