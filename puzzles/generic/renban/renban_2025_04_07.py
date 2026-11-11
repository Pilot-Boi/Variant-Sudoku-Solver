"""PuzzleMadness Renban Sudoku — 2025-04-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-04-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/4/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 7, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 6, 0, 4, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 3, 0, 0],
        [0, 2, 5, 3, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 5, 1, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 5, 0, 6, 4, 0],
        [0, 4, 0, 0, 0, 7, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 6), (4, 7), (4, 8), (3, 8), (2, 8)])
    puzzle.add_renban([(4, 1), (5, 2), (6, 3), (7, 4), (8, 5)])
    puzzle.add_renban([(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])
    puzzle.add_renban([(3, 4), (3, 5), (3, 6), (3, 7)])
    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(6, 6), (7, 6), (8, 6), (8, 7)])
    puzzle.add_renban([(0, 3), (1, 3), (2, 3)])
    puzzle.add_renban([(1, 7), (1, 6), (2, 6)])
    puzzle.add_renban([(8, 2), (8, 3), (8, 4)])
    puzzle.add_renban([(1, 5), (2, 4), (3, 3)])
    puzzle.add_renban([(7, 1), (6, 1)])
    puzzle.add_renban([(2, 1), (3, 1)])
    puzzle.add_renban([(4, 3), (4, 4)])
    puzzle.add_renban([(7, 8), (6, 8)])
    puzzle.add_renban([(6, 5), (5, 5)])

    return puzzle
