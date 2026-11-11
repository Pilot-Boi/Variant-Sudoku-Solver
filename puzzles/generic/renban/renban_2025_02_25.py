"""PuzzleMadness Renban Sudoku — 2025-02-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 4, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 3, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 4, 3],
        [0, 5, 3, 0, 0, 9, 0, 6, 0],
        [0, 0, 4, 5, 6, 0, 0, 0, 0],
        [0, 9, 1, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 2), (4, 3), (4, 4), (3, 4), (2, 4)])
    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(0, 5), (1, 5), (2, 5), (2, 6), (2, 7)])
    puzzle.add_renban([(2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(4, 8), (3, 8), (3, 7), (3, 6)])
    puzzle.add_renban([(4, 6), (5, 6), (5, 7), (5, 8)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2)])
    puzzle.add_renban([(3, 0), (4, 1), (5, 2)])
    puzzle.add_renban([(1, 2), (2, 3), (1, 4)])
    puzzle.add_renban([(7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(6, 3), (5, 3)])
    puzzle.add_renban([(6, 6), (6, 5)])
    puzzle.add_renban([(0, 2), (0, 3)])
    puzzle.add_renban([(0, 0), (0, 1)])
    puzzle.add_renban([(4, 0), (5, 1)])

    return puzzle
