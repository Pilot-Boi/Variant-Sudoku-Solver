"""PuzzleMadness Renban Sudoku — 2025-01-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-01-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/1/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 8, 0, 0, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 4, 1, 2, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 2, 0, 8, 9, 0, 0],
        [0, 0, 0, 9, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [4, 0, 9, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 3, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(1, 1), (2, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_renban([(4, 6), (5, 5), (6, 4), (7, 3), (8, 2)])
    puzzle.add_renban([(0, 4), (1, 5), (2, 6), (1, 7), (0, 8)])
    puzzle.add_renban([(6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_renban([(4, 4), (4, 5), (3, 5), (2, 5)])
    puzzle.add_renban([(8, 7), (7, 7), (6, 7), (6, 6)])
    puzzle.add_renban([(4, 1), (5, 2), (6, 3)])
    puzzle.add_renban([(8, 3), (8, 4), (7, 4)])
    puzzle.add_renban([(6, 1), (7, 1), (7, 2)])
    puzzle.add_renban([(1, 8), (2, 7), (3, 6)])
    puzzle.add_renban([(5, 0), (5, 1)])
    puzzle.add_renban([(3, 8), (4, 7)])
    puzzle.add_renban([(1, 3), (1, 4)])
    puzzle.add_renban([(8, 6), (8, 5)])
    puzzle.add_renban([(7, 5), (6, 5)])

    return puzzle
