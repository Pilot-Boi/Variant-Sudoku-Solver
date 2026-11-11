"""PuzzleMadness Renban Sudoku — 2025-12-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 7, 0, 0, 8],
        [0, 7, 9, 1, 0, 0, 0, 0, 4],
        [0, 0, 3, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 1],
        [0, 0, 5, 9, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 6, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 8), (1, 7), (1, 6), (2, 6), (3, 6)])
    puzzle.add_renban([(5, 5), (5, 6), (5, 7), (4, 7), (3, 7)])
    puzzle.add_renban([(6, 4), (7, 5), (8, 6), (7, 7), (6, 8)])
    puzzle.add_renban([(5, 2), (6, 2), (7, 2), (7, 3)])
    puzzle.add_renban([(1, 2), (2, 3), (1, 4), (0, 5)])
    puzzle.add_renban([(4, 6), (3, 5), (2, 4), (3, 3)])
    puzzle.add_renban([(2, 2), (3, 1), (4, 2)])
    puzzle.add_renban([(4, 1), (5, 0), (6, 1)])
    puzzle.add_renban([(4, 3), (4, 4), (4, 5)])
    puzzle.add_renban([(8, 0), (7, 0), (6, 0)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(0, 3), (0, 4)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(0, 1), (0, 2)])
    puzzle.add_renban([(1, 5), (2, 5)])

    return puzzle
