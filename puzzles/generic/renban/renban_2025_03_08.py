"""PuzzleMadness Renban Sudoku — 2025-03-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 3, 0, 0, 0, 0, 8],
        [0, 0, 0, 2, 0, 0, 4, 5, 7],
        [0, 0, 0, 6, 5, 8, 0, 0, 3],
        [0, 3, 0, 0, 8, 0, 0, 0, 4],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 7, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 6, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (6, 6), (5, 6)])
    puzzle.add_renban([(4, 5), (4, 4), (4, 3), (5, 3), (6, 3)])
    puzzle.add_renban([(8, 4), (8, 5), (8, 6), (8, 7), (8, 8)])
    puzzle.add_renban([(3, 6), (4, 6), (4, 7), (4, 8)])
    puzzle.add_renban([(2, 5), (1, 4), (2, 3), (3, 2)])
    puzzle.add_renban([(1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_renban([(7, 0), (6, 1), (5, 2)])
    puzzle.add_renban([(8, 1), (8, 2), (7, 2)])
    puzzle.add_renban([(3, 7), (3, 8), (2, 8)])
    puzzle.add_renban([(1, 2), (1, 1), (2, 1)])
    puzzle.add_renban([(8, 3), (7, 3)])
    puzzle.add_renban([(6, 4), (5, 4)])
    puzzle.add_renban([(6, 8), (5, 7)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(1, 7), (1, 6)])

    return puzzle
