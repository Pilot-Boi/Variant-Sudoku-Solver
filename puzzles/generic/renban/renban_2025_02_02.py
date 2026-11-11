"""PuzzleMadness Renban Sudoku — 2025-02-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 5, 6, 0, 0, 0, 4],
        [8, 0, 0, 4, 0, 2, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 4, 0, 0],
        [2, 9, 0, 0, 0, 3, 0, 0, 5],
        [0, 0, 0, 0, 5, 6, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 5, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (3, 3), (2, 3), (2, 2), (2, 1)])
    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (6, 5), (5, 5)])
    puzzle.add_renban([(5, 4), (4, 5), (3, 6), (2, 5), (1, 4)])
    puzzle.add_renban([(3, 2), (4, 2), (5, 2), (5, 3)])
    puzzle.add_renban([(2, 8), (1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(0, 1), (0, 2), (0, 3), (0, 4)])
    puzzle.add_renban([(6, 8), (5, 8), (5, 7)])
    puzzle.add_renban([(2, 6), (2, 7), (1, 7)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(1, 6), (1, 5)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(4, 0), (3, 1)])
    puzzle.add_renban([(6, 3), (6, 4)])
    puzzle.add_renban([(8, 2), (8, 3)])

    return puzzle
