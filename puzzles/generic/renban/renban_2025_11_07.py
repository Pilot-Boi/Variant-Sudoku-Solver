"""PuzzleMadness Renban Sudoku — 2025-11-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 5, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [0, 0, 9, 0, 2, 0, 0, 0, 0],
        [0, 4, 0, 0, 3, 0, 0, 6, 0],
        [8, 0, 2, 0, 0, 7, 0, 3, 0],
        [7, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 5, 0, 0, 9, 0, 2, 0, 0],
        [0, 3, 0, 4, 6, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 8), (1, 7), (0, 6), (1, 5), (2, 4)])
    puzzle.add_renban([(5, 7), (4, 7), (3, 7), (3, 6), (3, 5)])
    puzzle.add_renban([(4, 4), (5, 3), (6, 2), (7, 1), (8, 0)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (7, 0)])
    puzzle.add_renban([(2, 0), (3, 1), (4, 2), (3, 3)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6), (7, 5)])
    puzzle.add_renban([(4, 3), (3, 4), (2, 3)])
    puzzle.add_renban([(3, 0), (4, 1), (5, 2)])
    puzzle.add_renban([(6, 6), (5, 6), (5, 5)])
    puzzle.add_renban([(1, 6), (2, 6), (2, 7)])
    puzzle.add_renban([(8, 5), (7, 4)])
    puzzle.add_renban([(8, 4), (7, 3)])
    puzzle.add_renban([(1, 2), (2, 2)])
    puzzle.add_renban([(3, 8), (4, 8)])
    puzzle.add_renban([(0, 4), (0, 5)])

    return puzzle
