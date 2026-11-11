"""PuzzleMadness Renban Sudoku — 2025-03-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 1, 0, 4, 0, 0, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 5, 0],
        [0, 7, 0, 0, 1, 0, 3, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 9, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 8, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 0), (6, 1), (6, 2), (6, 3), (6, 4)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5), (6, 6), (6, 7)])
    puzzle.add_renban([(2, 8), (1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_renban([(1, 6), (1, 5), (2, 5), (3, 5)])
    puzzle.add_renban([(2, 4), (1, 4), (0, 4), (0, 3)])
    puzzle.add_renban([(5, 6), (5, 7), (5, 8), (4, 8)])
    puzzle.add_renban([(3, 4), (4, 3), (5, 2)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(4, 0), (4, 1), (4, 2)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(1, 7), (2, 6)])
    puzzle.add_renban([(1, 1), (2, 2)])
    puzzle.add_renban([(3, 0), (3, 1)])
    puzzle.add_renban([(5, 0), (5, 1)])
    puzzle.add_renban([(2, 7), (3, 6)])

    return puzzle
