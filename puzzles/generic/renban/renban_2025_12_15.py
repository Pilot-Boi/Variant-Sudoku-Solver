"""PuzzleMadness Renban Sudoku — 2025-12-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 8, 0, 0],
        [3, 0, 0, 6, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 1, 0, 0, 0, 3],
        [0, 8, 0, 0, 3, 0, 0, 0, 6],
        [6, 0, 5, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 2, 0, 0, 0, 5],
        [0, 7, 0, 0, 0, 0, 0, 9, 0],
        [5, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 1), (4, 2), (4, 3), (3, 3), (2, 3)])
    puzzle.add_renban([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_renban([(1, 4), (0, 4), (0, 3), (0, 2)])
    puzzle.add_renban([(8, 6), (7, 6), (6, 6), (5, 6)])
    puzzle.add_renban([(2, 6), (2, 7), (1, 7), (0, 7)])
    puzzle.add_renban([(7, 3), (6, 3), (5, 3)])
    puzzle.add_renban([(1, 1), (1, 0), (2, 0)])
    puzzle.add_renban([(8, 7), (8, 8), (7, 8)])
    puzzle.add_renban([(1, 3), (1, 2), (2, 2)])
    puzzle.add_renban([(4, 8), (5, 8)])
    puzzle.add_renban([(4, 0), (5, 0)])
    puzzle.add_renban([(3, 7), (4, 7)])
    puzzle.add_renban([(6, 2), (5, 2)])
    puzzle.add_renban([(6, 7), (5, 7)])

    return puzzle
