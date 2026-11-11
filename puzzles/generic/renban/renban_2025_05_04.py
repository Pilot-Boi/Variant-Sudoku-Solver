"""PuzzleMadness Renban Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 2, 0, 1, 5],
        [2, 4, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 9, 8, 3, 0],
        [8, 0, 2, 0, 0, 0, 0, 0, 6],
        [1, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 6), (4, 5), (4, 4), (5, 4), (6, 4)])
    puzzle.add_renban([(6, 2), (6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_renban([(5, 5), (6, 5), (7, 5), (7, 6), (7, 7)])
    puzzle.add_renban([(0, 8), (1, 7), (2, 6), (3, 7)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3), (2, 4)])
    puzzle.add_renban([(3, 4), (3, 3), (3, 2), (4, 2)])
    puzzle.add_renban([(7, 1), (8, 1), (8, 2)])
    puzzle.add_renban([(4, 1), (5, 1), (5, 2)])
    puzzle.add_renban([(5, 8), (4, 7), (3, 6)])
    puzzle.add_renban([(7, 4), (8, 4), (8, 5)])
    puzzle.add_renban([(0, 1), (1, 1)])
    puzzle.add_renban([(2, 8), (2, 7)])
    puzzle.add_renban([(1, 6), (1, 5)])
    puzzle.add_renban([(5, 7), (5, 6)])
    puzzle.add_renban([(8, 8), (7, 8)])

    return puzzle
