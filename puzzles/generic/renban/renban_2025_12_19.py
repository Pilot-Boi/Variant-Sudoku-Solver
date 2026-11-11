"""PuzzleMadness Renban Sudoku — 2025-12-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 2, 0, 1, 8, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 3, 0, 0, 6],
        [0, 6, 1, 0, 8, 0, 0, 3, 5],
        [0, 0, 0, 6, 0, 0, 9, 0, 0],
        [0, 0, 5, 0, 0, 2, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 3), (3, 3), (2, 3), (2, 2), (2, 1)])
    puzzle.add_renban([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (6, 8), (7, 8)])
    puzzle.add_renban([(5, 4), (5, 5), (4, 5), (3, 5)])
    puzzle.add_renban([(8, 1), (7, 1), (6, 1), (5, 1)])
    puzzle.add_renban([(5, 3), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(6, 3), (7, 4), (6, 5)])
    puzzle.add_renban([(4, 6), (4, 7), (3, 7)])
    puzzle.add_renban([(2, 8), (2, 7), (2, 6)])
    puzzle.add_renban([(5, 0), (4, 1), (3, 2)])
    puzzle.add_renban([(3, 4), (4, 4)])
    puzzle.add_renban([(8, 7), (7, 7)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(0, 2), (0, 3)])
    puzzle.add_renban([(8, 2), (7, 3)])

    return puzzle
