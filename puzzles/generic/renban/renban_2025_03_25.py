"""PuzzleMadness Renban Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 5, 9],
        [0, 2, 5, 0, 0, 0, 0, 3, 0],
        [8, 0, 0, 0, 0, 9, 0, 0, 6],
        [0, 0, 0, 0, 3, 0, 0, 0, 1],
        [0, 0, 7, 2, 8, 0, 5, 0, 0],
        [0, 0, 1, 4, 6, 0, 0, 0, 3],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 7), (4, 6), (4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(0, 6), (0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_renban([(2, 0), (2, 1), (2, 2), (1, 2), (0, 2)])
    puzzle.add_renban([(7, 2), (7, 3), (7, 4), (6, 4)])
    puzzle.add_renban([(3, 0), (4, 1), (5, 2), (4, 3)])
    puzzle.add_renban([(0, 8), (1, 8), (2, 8), (3, 8)])
    puzzle.add_renban([(4, 4), (3, 3), (4, 2)])
    puzzle.add_renban([(5, 1), (6, 0), (7, 1)])
    puzzle.add_renban([(7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(0, 7), (1, 7), (2, 7)])
    puzzle.add_renban([(0, 1), (1, 1)])
    puzzle.add_renban([(8, 8), (7, 7)])
    puzzle.add_renban([(4, 8), (3, 7)])
    puzzle.add_renban([(6, 7), (5, 7)])
    puzzle.add_renban([(1, 6), (1, 5)])

    return puzzle
