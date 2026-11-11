"""PuzzleMadness Renban Sudoku — 2025-06-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-06-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/6/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 9, 0, 3],
        [1, 0, 0, 0, 0, 7, 0, 6, 4],
        [0, 6, 0, 0, 0, 3, 0, 0, 0],
        [9, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 6, 0, 0, 0, 0, 4, 0],
        [3, 4, 0, 0, 0, 6, 0, 0, 8],
        [0, 0, 8, 9, 0, 0, 3, 5, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6)])
    puzzle.add_renban([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (7, 7), (7, 8)])
    puzzle.add_renban([(1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_renban([(5, 0), (5, 1), (5, 2), (5, 3)])
    puzzle.add_renban([(2, 7), (2, 8), (1, 8), (0, 8)])
    puzzle.add_renban([(6, 2), (7, 2), (7, 3)])
    puzzle.add_renban([(0, 1), (1, 1), (2, 1)])
    puzzle.add_renban([(6, 1), (6, 0), (7, 0)])
    puzzle.add_renban([(3, 1), (4, 1), (4, 2)])
    puzzle.add_renban([(3, 8), (3, 7)])
    puzzle.add_renban([(6, 8), (6, 7)])
    puzzle.add_renban([(4, 7), (5, 7)])
    puzzle.add_renban([(2, 0), (3, 0)])
    puzzle.add_renban([(6, 4), (6, 5)])

    return puzzle
