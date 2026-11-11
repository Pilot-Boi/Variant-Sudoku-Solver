"""PuzzleMadness Renban Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 5, 0, 0],
        [4, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 2, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 2, 0, 0, 0, 1],
        [0, 0, 0, 5, 0, 0, 0, 3, 0],
        [0, 0, 0, 6, 9, 0, 0, 0, 8],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 5), (5, 6), (4, 7), (3, 6), (2, 5)])
    puzzle.add_renban([(4, 4), (4, 3), (4, 2), (5, 2), (6, 2)])
    puzzle.add_renban([(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)])
    puzzle.add_renban([(7, 4), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(8, 8), (7, 8), (6, 8), (6, 7)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(2, 1), (3, 0), (4, 1)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2)])
    puzzle.add_renban([(7, 5), (7, 6), (6, 6)])
    puzzle.add_renban([(6, 1), (7, 2), (6, 3)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(2, 7), (2, 6)])
    puzzle.add_renban([(3, 2), (3, 3)])
    puzzle.add_renban([(4, 5), (5, 5)])

    return puzzle
