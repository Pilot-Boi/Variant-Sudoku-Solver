"""PuzzleMadness Renban Sudoku — 2025-05-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 9, 0, 0, 0, 0, 6],
        [0, 0, 8, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 5, 6, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 6, 0, 1, 0, 0, 0],
        [0, 2, 0, 0, 0, 7, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 4), (2, 5), (2, 6), (2, 7), (2, 8)])
    puzzle.add_renban([(5, 1), (6, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(2, 2), (3, 2), (4, 2), (5, 2)])
    puzzle.add_renban([(5, 5), (5, 6), (4, 6), (3, 6)])
    puzzle.add_renban([(5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_renban([(0, 3), (0, 2), (1, 2)])
    puzzle.add_renban([(3, 4), (4, 4), (4, 5)])
    puzzle.add_renban([(3, 0), (4, 0), (5, 0)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6)])
    puzzle.add_renban([(6, 8), (6, 7)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(0, 6), (1, 6)])
    puzzle.add_renban([(7, 4), (7, 5)])
    puzzle.add_renban([(0, 1), (1, 1)])

    return puzzle
