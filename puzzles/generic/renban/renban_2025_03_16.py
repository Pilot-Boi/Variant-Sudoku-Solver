"""PuzzleMadness Renban Sudoku — 2025-03-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 9, 0, 1, 0, 0, 7],
        [4, 0, 0, 8, 0, 0, 0, 1, 5],
        [0, 0, 0, 0, 2, 5, 0, 4, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 8],
        [2, 8, 0, 1, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [7, 1, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 6), (4, 6), (5, 6), (5, 7), (5, 8)])
    puzzle.add_renban([(8, 1), (8, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_renban([(2, 3), (3, 2), (4, 1), (5, 2), (6, 3)])
    puzzle.add_renban([(1, 5), (2, 4), (3, 3), (4, 2)])
    puzzle.add_renban([(0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_renban([(4, 5), (5, 5), (6, 5), (7, 5)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(3, 1), (4, 0), (5, 1)])
    puzzle.add_renban([(1, 1), (2, 2), (1, 3)])
    puzzle.add_renban([(8, 6), (8, 7), (7, 7)])
    puzzle.add_renban([(0, 2), (0, 3)])
    puzzle.add_renban([(6, 8), (6, 7)])
    puzzle.add_renban([(6, 0), (6, 1)])
    puzzle.add_renban([(8, 0), (7, 0)])
    puzzle.add_renban([(4, 8), (3, 7)])

    return puzzle
