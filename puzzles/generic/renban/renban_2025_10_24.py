"""PuzzleMadness Renban Sudoku — 2025-10-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [4, 0, 1, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 8, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 6, 2, 0, 7, 8],
        [0, 0, 3, 0, 0, 0, 0, 0, 6],
        [0, 1, 0, 5, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 6), (1, 6), (0, 6), (0, 5), (0, 4)])
    puzzle.add_renban([(3, 8), (3, 7), (3, 6), (4, 6), (5, 6)])
    puzzle.add_renban([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_renban([(5, 5), (5, 4), (5, 3), (6, 3)])
    puzzle.add_renban([(4, 2), (4, 3), (3, 3), (2, 3)])
    puzzle.add_renban([(4, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(1, 8), (0, 8), (0, 7)])
    puzzle.add_renban([(5, 8), (4, 8), (4, 7)])
    puzzle.add_renban([(1, 2), (1, 3)])
    puzzle.add_renban([(4, 1), (3, 2)])
    puzzle.add_renban([(3, 5), (4, 5)])
    puzzle.add_renban([(7, 3), (7, 4)])
    puzzle.add_renban([(3, 0), (3, 1)])

    return puzzle
