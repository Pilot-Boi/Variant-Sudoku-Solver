"""PuzzleMadness Renban Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 7, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 2, 8],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 2, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 8, 0, 3, 0, 0, 0],
        [0, 0, 0, 6, 0, 7, 0, 0, 0],
        [0, 0, 2, 0, 3, 0, 0, 0, 0],
        [7, 4, 3, 9, 0, 0, 0, 5, 0],
        [9, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)])
    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(3, 3), (4, 3), (5, 3), (5, 4), (5, 5)])
    puzzle.add_renban([(3, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_renban([(6, 1), (6, 2), (6, 3), (6, 4)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(1, 7), (1, 6), (1, 5)])
    puzzle.add_renban([(3, 6), (2, 6), (2, 5)])
    puzzle.add_renban([(5, 8), (5, 7), (5, 6)])
    puzzle.add_renban([(4, 2), (4, 1), (5, 1)])
    puzzle.add_renban([(1, 3), (1, 4)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(6, 8), (6, 7)])
    puzzle.add_renban([(8, 8), (7, 8)])
    puzzle.add_renban([(2, 2), (3, 2)])

    return puzzle
