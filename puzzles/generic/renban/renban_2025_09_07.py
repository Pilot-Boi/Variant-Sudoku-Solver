"""PuzzleMadness Renban Sudoku — 2025-09-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-09-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/9/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 8, 0, 3, 0, 5, 1, 0],
        [0, 0, 0, 0, 7, 0, 0, 2, 0],
        [0, 0, 0, 0, 1, 0, 0, 6, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 2, 9, 6, 0, 0, 0, 3],
        [0, 0, 0, 2, 0, 0, 6, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 7), (3, 7), (2, 7), (2, 6), (2, 5)])
    puzzle.add_renban([(6, 5), (5, 5), (4, 5), (4, 4), (4, 3)])
    puzzle.add_renban([(3, 2), (4, 2), (5, 2), (6, 2), (7, 2)])
    puzzle.add_renban([(7, 4), (7, 5), (7, 6), (7, 7)])
    puzzle.add_renban([(5, 8), (5, 7), (5, 6), (6, 6)])
    puzzle.add_renban([(8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_renban([(3, 3), (2, 4), (1, 3)])
    puzzle.add_renban([(0, 1), (0, 0), (1, 0)])
    puzzle.add_renban([(2, 1), (2, 0), (3, 0)])
    puzzle.add_renban([(4, 6), (3, 6), (3, 5)])
    puzzle.add_renban([(6, 4), (5, 3)])
    puzzle.add_renban([(0, 8), (1, 8)])
    puzzle.add_renban([(1, 4), (1, 5)])
    puzzle.add_renban([(0, 2), (1, 2)])
    puzzle.add_renban([(7, 0), (7, 1)])

    return puzzle
