"""PuzzleMadness Renban Sudoku — 2025-08-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-08-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/8/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 8, 0, 5, 0, 0, 0, 6],
        [0, 0, 5, 0, 0, 0, 0, 0, 2],
        [7, 0, 0, 0, 0, 5, 0, 6, 0],
        [2, 0, 0, 7, 0, 0, 0, 0, 0],
        [8, 4, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 6, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 4), (1, 3), (1, 2), (2, 2), (3, 2)])
    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(7, 4), (6, 3), (5, 2), (6, 1)])
    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(4, 4), (3, 4), (3, 3)])
    puzzle.add_renban([(7, 1), (7, 2), (7, 3)])
    puzzle.add_renban([(4, 6), (5, 6), (5, 7)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7)])
    puzzle.add_renban([(0, 7), (1, 7)])
    puzzle.add_renban([(3, 1), (4, 1)])
    puzzle.add_renban([(1, 0), (2, 1)])
    puzzle.add_renban([(3, 8), (4, 8)])
    puzzle.add_renban([(1, 6), (1, 5)])

    return puzzle
