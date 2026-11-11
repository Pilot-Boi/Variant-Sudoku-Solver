"""PuzzleMadness Renban Sudoku — 2025-06-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 2, 1, 0],
        [0, 5, 0, 0, 0, 0, 4, 0, 0],
        [0, 1, 0, 0, 4, 2, 0, 0, 6],
        [2, 0, 0, 0, 0, 0, 0, 6, 8],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 7, 4, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(6, 5), (7, 5), (8, 5), (8, 6), (8, 7)])
    puzzle.add_renban([(0, 6), (1, 5), (2, 4), (3, 5), (4, 6)])
    puzzle.add_renban([(4, 0), (5, 0), (6, 0), (6, 1), (6, 2)])
    puzzle.add_renban([(4, 5), (5, 4), (6, 3), (7, 2)])
    puzzle.add_renban([(3, 7), (2, 7), (1, 7), (1, 6)])
    puzzle.add_renban([(0, 0), (0, 1), (0, 2), (0, 3)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(7, 1), (8, 2), (7, 3)])
    puzzle.add_renban([(1, 8), (2, 8), (3, 8)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(4, 7), (5, 6)])
    puzzle.add_renban([(5, 1), (5, 2)])
    puzzle.add_renban([(3, 0), (4, 1)])
    puzzle.add_renban([(8, 4), (7, 4)])
    puzzle.add_renban([(4, 3), (4, 4)])

    return puzzle
