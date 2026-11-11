"""PuzzleMadness Renban Sudoku — 2025-12-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 5, 0],
        [0, 0, 6, 0, 8, 0, 0, 0, 2],
        [0, 0, 7, 0, 0, 0, 8, 0, 0],
        [0, 6, 0, 9, 1, 0, 7, 0, 0],
        [0, 7, 4, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 0, 5, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 7, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 2), (1, 1), (2, 0), (3, 1), (4, 2)])
    puzzle.add_renban([(2, 6), (3, 6), (4, 6), (4, 7), (4, 8)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (8, 7), (8, 8)])
    puzzle.add_renban([(1, 2), (2, 2), (3, 2), (3, 3)])
    puzzle.add_renban([(6, 2), (6, 3), (5, 3), (4, 3)])
    puzzle.add_renban([(5, 7), (5, 6), (6, 6), (7, 6)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(6, 4), (6, 5), (5, 5)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(4, 4), (4, 5), (3, 5)])
    puzzle.add_renban([(8, 3), (7, 3)])
    puzzle.add_renban([(3, 8), (3, 7)])
    puzzle.add_renban([(2, 3), (2, 4)])
    puzzle.add_renban([(8, 0), (8, 1)])
    puzzle.add_renban([(0, 4), (1, 4)])

    return puzzle
