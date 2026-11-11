"""PuzzleMadness Renban Sudoku — 2025-02-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-02-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/2/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 9, 0],
        [0, 0, 0, 6, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 5, 7, 0, 0],
        [7, 0, 3, 0, 0, 2, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [4, 0, 9, 0, 1, 0, 0, 7, 0],
        [0, 0, 0, 0, 9, 4, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 4), (4, 3), (5, 2), (6, 1), (7, 0)])
    puzzle.add_renban([(3, 5), (2, 5), (1, 5), (1, 4), (1, 3)])
    puzzle.add_renban([(3, 7), (4, 7), (5, 7), (6, 7), (7, 7)])
    puzzle.add_renban([(0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(2, 3), (2, 2), (3, 2), (4, 2)])
    puzzle.add_renban([(7, 3), (6, 4), (5, 5)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7)])
    puzzle.add_renban([(2, 7), (2, 6), (3, 6)])
    puzzle.add_renban([(0, 1), (1, 2)])
    puzzle.add_renban([(8, 8), (7, 8)])
    puzzle.add_renban([(8, 0), (7, 1)])
    puzzle.add_renban([(8, 2), (8, 3)])
    puzzle.add_renban([(4, 4), (5, 3)])

    return puzzle
