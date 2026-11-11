"""PuzzleMadness Renban Sudoku — 2025-11-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 1, 0, 0, 3, 9, 0, 7, 4],
        [0, 0, 0, 0, 0, 7, 0, 0, 5],
        [0, 3, 0, 0, 1, 0, 8, 0, 0],
        [0, 7, 0, 8, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 7, 6, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 9, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(4, 7), (5, 6), (6, 5), (7, 6), (8, 7)])
    puzzle.add_renban([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])
    puzzle.add_renban([(5, 1), (6, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(3, 3), (4, 3), (5, 3), (5, 4)])
    puzzle.add_renban([(4, 6), (3, 7), (2, 6)])
    puzzle.add_renban([(1, 3), (1, 4), (1, 5)])
    puzzle.add_renban([(1, 8), (2, 7)])
    puzzle.add_renban([(3, 8), (4, 8)])
    puzzle.add_renban([(3, 1), (4, 1)])
    puzzle.add_renban([(6, 3), (6, 4)])
    puzzle.add_renban([(7, 8), (6, 7)])

    return puzzle
