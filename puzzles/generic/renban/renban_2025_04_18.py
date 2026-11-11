"""PuzzleMadness Renban Sudoku — 2025-04-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 2, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 6, 0, 3, 0, 8],
        [0, 0, 0, 0, 5, 0, 1, 0, 0],
        [0, 0, 8, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 2, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 8, 0, 0, 0, 5, 0, 0, 0],
        [0, 1, 0, 0, 3, 6, 5, 0, 0],
        [0, 4, 0, 2, 8, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (6, 8), (7, 8)])
    puzzle.add_renban([(4, 4), (3, 4), (2, 4), (2, 3), (2, 2)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(3, 6), (2, 6), (1, 6), (1, 5)])
    puzzle.add_renban([(2, 0), (3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(7, 2), (6, 2), (6, 1)])
    puzzle.add_renban([(7, 4), (6, 3), (5, 2)])
    puzzle.add_renban([(1, 7), (0, 7), (0, 6)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(7, 6), (7, 5)])
    puzzle.add_renban([(2, 8), (3, 7)])
    puzzle.add_renban([(5, 7), (5, 6)])
    puzzle.add_renban([(6, 7), (6, 6)])

    return puzzle
