"""PuzzleMadness Renban Sudoku — 2025-03-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-03-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/3/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 5, 4],
        [3, 0, 0, 0, 0, 0, 0, 0, 9],
        [5, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 9, 8, 0, 0, 0],
        [7, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 3, 0, 0, 0, 1],
        [0, 0, 8, 0, 0, 0, 7, 6, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 7), (1, 6), (0, 5), (1, 4), (2, 3)])
    puzzle.add_renban([(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
    puzzle.add_renban([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
    puzzle.add_renban([(5, 1), (6, 2), (7, 3), (6, 4)])
    puzzle.add_renban([(7, 8), (7, 7), (7, 6)])
    puzzle.add_renban([(4, 8), (3, 7), (2, 6)])
    puzzle.add_renban([(6, 0), (7, 0), (7, 1)])
    puzzle.add_renban([(5, 2), (6, 3), (5, 4)])
    puzzle.add_renban([(0, 1), (1, 1)])
    puzzle.add_renban([(0, 2), (1, 2)])
    puzzle.add_renban([(5, 6), (5, 5)])
    puzzle.add_renban([(8, 4), (7, 4)])
    puzzle.add_renban([(3, 4), (3, 5)])

    return puzzle
