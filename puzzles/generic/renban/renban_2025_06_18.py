"""PuzzleMadness Renban Sudoku — 2025-06-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 5, 2, 0, 0, 0, 4, 0],
        [8, 4, 7, 0, 0, 6, 0, 0, 1],
        [0, 0, 8, 4, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 2],
        [3, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_renban([(2, 5), (2, 4), (2, 3), (3, 3), (4, 3)])
    puzzle.add_renban([(4, 2), (4, 1), (4, 0), (5, 0)])
    puzzle.add_renban([(7, 5), (6, 6), (5, 7), (4, 6)])
    puzzle.add_renban([(1, 3), (1, 2), (1, 1), (2, 1)])
    puzzle.add_renban([(5, 2), (5, 1), (6, 1)])
    puzzle.add_renban([(6, 4), (6, 5), (5, 5)])
    puzzle.add_renban([(1, 7), (2, 6), (3, 7)])
    puzzle.add_renban([(8, 8), (8, 7), (8, 6)])
    puzzle.add_renban([(3, 4), (3, 5)])
    puzzle.add_renban([(2, 0), (3, 0)])
    puzzle.add_renban([(1, 6), (1, 5)])
    puzzle.add_renban([(3, 6), (4, 5)])
    puzzle.add_renban([(8, 3), (8, 4)])

    return puzzle
