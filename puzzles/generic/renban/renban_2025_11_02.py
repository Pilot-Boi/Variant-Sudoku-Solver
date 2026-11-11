"""PuzzleMadness Renban Sudoku — 2025-11-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 3, 0, 0, 0, 0, 1, 9],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 5, 0, 2, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 7, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 2, 8, 0, 0],
        [7, 9, 0, 0, 0, 0, 0, 0, 5],
        [6, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 3), (3, 2), (4, 1), (5, 2), (6, 3)])
    puzzle.add_renban([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5)])
    puzzle.add_renban([(7, 6), (7, 7), (7, 8), (6, 8)])
    puzzle.add_renban([(1, 7), (2, 7), (3, 7), (4, 7)])
    puzzle.add_renban([(4, 2), (3, 3), (2, 4), (1, 3)])
    puzzle.add_renban([(1, 1), (2, 0), (3, 1)])
    puzzle.add_renban([(4, 6), (5, 6), (5, 7)])
    puzzle.add_renban([(0, 8), (1, 8), (2, 8)])
    puzzle.add_renban([(8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(6, 1), (5, 1)])
    puzzle.add_renban([(4, 4), (5, 4)])
    puzzle.add_renban([(4, 0), (5, 0)])
    puzzle.add_renban([(6, 7), (6, 6)])
    puzzle.add_renban([(3, 4), (4, 3)])

    return puzzle
