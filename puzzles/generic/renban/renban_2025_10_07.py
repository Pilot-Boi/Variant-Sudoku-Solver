"""PuzzleMadness Renban Sudoku — 2025-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 9, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 0, 8, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 8, 0, 2, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 5, 0, 3, 0, 1, 0, 9],
        [0, 0, 4, 0, 0, 6, 2, 0, 0],
        [0, 0, 3, 0, 9, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 5), (1, 4), (2, 3), (3, 4), (4, 5)])
    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_renban([(5, 0), (5, 1), (5, 2), (5, 3), (5, 4)])
    puzzle.add_renban([(3, 6), (2, 6), (2, 5), (2, 4)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (7, 5)])
    puzzle.add_renban([(3, 8), (4, 8), (5, 8), (6, 8)])
    puzzle.add_renban([(5, 6), (6, 6), (6, 7)])
    puzzle.add_renban([(6, 3), (6, 4), (6, 5)])
    puzzle.add_renban([(3, 1), (3, 0), (4, 0)])
    puzzle.add_renban([(1, 7), (1, 6), (1, 5)])
    puzzle.add_renban([(8, 8), (7, 8)])
    puzzle.add_renban([(0, 0), (1, 1)])
    puzzle.add_renban([(7, 3), (7, 4)])
    puzzle.add_renban([(0, 1), (0, 2)])
    puzzle.add_renban([(2, 1), (2, 2)])

    return puzzle
