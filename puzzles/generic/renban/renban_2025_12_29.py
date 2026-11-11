"""PuzzleMadness Renban Sudoku — 2025-12-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-12-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/12/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 3, 0, 0, 7],
        [2, 0, 0, 7, 0, 5, 8, 3, 0],
        [0, 0, 0, 0, 6, 0, 4, 0, 0],
        [3, 0, 0, 0, 0, 1, 0, 5, 0],
        [5, 1, 0, 0, 4, 0, 0, 0, 6],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(7, 3), (7, 4), (7, 5), (6, 5), (5, 5)])
    puzzle.add_renban([(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)])
    puzzle.add_renban([(0, 8), (1, 7), (2, 6), (3, 7), (4, 8)])
    puzzle.add_renban([(6, 6), (6, 7), (5, 7), (4, 7)])
    puzzle.add_renban([(2, 4), (3, 4), (4, 4), (5, 4)])
    puzzle.add_renban([(1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_renban([(1, 0), (2, 0), (2, 1)])
    puzzle.add_renban([(3, 0), (4, 1), (5, 2)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(7, 8), (6, 8), (5, 8)])
    puzzle.add_renban([(1, 6), (2, 5)])
    puzzle.add_renban([(3, 2), (4, 3)])
    puzzle.add_renban([(8, 7), (7, 6)])
    puzzle.add_renban([(4, 6), (5, 6)])
    puzzle.add_renban([(5, 0), (5, 1)])

    return puzzle
