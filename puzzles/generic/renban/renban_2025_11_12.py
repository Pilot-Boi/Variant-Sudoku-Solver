"""PuzzleMadness Renban Sudoku — 2025-11-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-11-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/11/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 2, 0, 0, 0, 0, 0, 0, 7],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 9, 0, 0, 0, 0, 4],
        [0, 0, 2, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 5, 0],
        [0, 7, 0, 2, 0, 6, 0, 0, 1],
        [0, 8, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 8, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(2, 5), (3, 5), (4, 5), (5, 5), (6, 5)])
    puzzle.add_renban([(0, 8), (0, 7), (0, 6), (1, 6), (2, 6)])
    puzzle.add_renban([(4, 4), (5, 3), (6, 2), (7, 3), (8, 4)])
    puzzle.add_renban([(1, 1), (2, 0), (3, 1), (4, 2)])
    puzzle.add_renban([(2, 4), (1, 4), (1, 3), (1, 2)])
    puzzle.add_renban([(4, 7), (5, 6), (6, 7), (7, 8)])
    puzzle.add_renban([(3, 0), (4, 0), (4, 1)])
    puzzle.add_renban([(2, 8), (3, 8), (4, 8)])
    puzzle.add_renban([(7, 1), (6, 1), (5, 1)])
    puzzle.add_renban([(4, 3), (3, 3), (3, 2)])
    puzzle.add_renban([(2, 7), (3, 6)])
    puzzle.add_renban([(6, 0), (5, 0)])
    puzzle.add_renban([(0, 4), (1, 5)])

    return puzzle
