"""PuzzleMadness Renban Sudoku — 2025-12-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 5, 1, 0, 0, 0, 0],
        [0, 5, 0, 3, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 5, 0, 9, 0],
        [0, 0, 0, 0, 8, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 3],
        [0, 0, 0, 0, 0, 0, 8, 0, 6],
        [5, 2, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 1), (4, 2), (4, 3), (3, 3), (2, 3)])
    puzzle.add_renban([(1, 4), (2, 4), (3, 4), (3, 5), (3, 6)])
    puzzle.add_renban([(3, 8), (2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_renban([(7, 8), (6, 8), (6, 7), (6, 6)])
    puzzle.add_renban([(6, 4), (7, 4), (8, 4), (8, 5)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (2, 1)])
    puzzle.add_renban([(4, 6), (5, 6), (5, 7)])
    puzzle.add_renban([(4, 5), (4, 4), (5, 4)])
    puzzle.add_renban([(5, 8), (4, 8), (4, 7)])
    puzzle.add_renban([(1, 2), (0, 2), (0, 1)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(8, 8), (8, 7)])
    puzzle.add_renban([(4, 0), (5, 1)])
    puzzle.add_renban([(8, 3), (7, 3)])
    puzzle.add_renban([(8, 1), (7, 2)])

    return puzzle
