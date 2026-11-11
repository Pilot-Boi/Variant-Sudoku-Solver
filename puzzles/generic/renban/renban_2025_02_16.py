"""PuzzleMadness Renban Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 2, 0, 1, 0, 4, 0],
        [6, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 1, 0, 0, 0, 9, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 9, 4, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 9, 1, 0, 8, 2, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 8), (3, 8), (2, 8), (2, 7), (2, 6)])
    puzzle.add_renban([(3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    puzzle.add_renban([(1, 4), (1, 3), (1, 2), (2, 2), (3, 2)])
    puzzle.add_renban([(2, 3), (3, 4), (4, 5), (5, 6)])
    puzzle.add_renban([(6, 3), (6, 4), (6, 5), (5, 5)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_renban([(0, 6), (1, 5), (2, 4)])
    puzzle.add_renban([(6, 6), (7, 6), (7, 7)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(4, 3), (4, 2), (5, 2)])
    puzzle.add_renban([(8, 2), (7, 2)])
    puzzle.add_renban([(3, 7), (4, 7)])
    puzzle.add_renban([(1, 8), (1, 7)])
    puzzle.add_renban([(1, 0), (1, 1)])
    puzzle.add_renban([(4, 0), (5, 0)])

    return puzzle
