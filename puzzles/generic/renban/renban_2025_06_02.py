"""PuzzleMadness Renban Sudoku — 2025-06-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 5, 4, 0],
        [4, 0, 2, 0, 0, 6, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 4, 8, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 5, 0, 0, 0, 9],
        [0, 6, 0, 1, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)])
    puzzle.add_renban([(1, 6), (2, 5), (3, 4), (4, 5), (5, 6)])
    puzzle.add_renban([(3, 3), (4, 3), (5, 3), (6, 3), (7, 3)])
    puzzle.add_renban([(4, 2), (5, 1), (6, 0), (7, 1)])
    puzzle.add_renban([(2, 3), (1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(2, 7), (3, 6), (4, 7), (5, 8)])
    puzzle.add_renban([(7, 5), (7, 6), (6, 6)])
    puzzle.add_renban([(7, 7), (6, 8), (5, 7)])
    puzzle.add_renban([(8, 1), (8, 2), (7, 2)])
    puzzle.add_renban([(1, 5), (1, 4), (2, 4)])
    puzzle.add_renban([(3, 1), (4, 1)])
    puzzle.add_renban([(4, 0), (5, 0)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(2, 8), (3, 7)])
    puzzle.add_renban([(2, 0), (2, 1)])

    return puzzle
