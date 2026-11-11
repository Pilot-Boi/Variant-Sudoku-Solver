"""PuzzleMadness Renban Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [9, 0, 0, 1, 3, 0, 0, 5, 0],
        [0, 5, 0, 2, 9, 8, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 5, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [6, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 5, 0, 0, 7, 0, 0, 0],
        [0, 2, 0, 0, 8, 0, 6, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 3), (1, 4), (1, 5), (1, 6), (1, 7)])
    puzzle.add_renban([(6, 2), (6, 3), (6, 4), (5, 4), (4, 4)])
    puzzle.add_renban([(7, 2), (7, 3), (7, 4), (7, 5), (7, 6)])
    puzzle.add_renban([(4, 8), (5, 8), (6, 8), (7, 8)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(3, 2), (4, 2), (5, 2), (5, 3)])
    puzzle.add_renban([(0, 8), (1, 8), (2, 8)])
    puzzle.add_renban([(4, 5), (3, 5), (3, 4)])
    puzzle.add_renban([(3, 7), (4, 6), (5, 7)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2)])
    puzzle.add_renban([(8, 4), (8, 5)])
    puzzle.add_renban([(3, 3), (4, 3)])
    puzzle.add_renban([(2, 4), (2, 5)])
    puzzle.add_renban([(1, 1), (1, 2)])
    puzzle.add_renban([(4, 0), (5, 0)])

    return puzzle
