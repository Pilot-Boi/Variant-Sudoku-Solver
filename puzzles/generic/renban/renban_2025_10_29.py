"""PuzzleMadness Renban Sudoku — 2025-10-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Renban Sudoku — 2025-10-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/renbansudoku/hard/2025/10/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 0, 0, 0, 8],
        [0, 0, 1, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 6],
        [0, 0, 0, 0, 4, 0, 0, 8, 0],
        [0, 2, 0, 8, 0, 0, 4, 1, 0],
        [0, 0, 0, 7, 0, 0, 3, 0, 0],
        [0, 0, 4, 9, 0, 0, 0, 0, 0],
        [7, 0, 9, 0, 0, 4, 0, 0, 5],
        [3, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_renban([(3, 4), (4, 4), (5, 4), (5, 5), (5, 6)])
    puzzle.add_renban([(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)])
    puzzle.add_renban([(2, 3), (1, 3), (0, 3), (0, 2)])
    puzzle.add_renban([(2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_renban([(4, 2), (4, 1), (5, 1), (6, 1)])
    puzzle.add_renban([(4, 6), (3, 6), (3, 5)])
    puzzle.add_renban([(5, 7), (4, 8), (3, 7)])
    puzzle.add_renban([(7, 4), (7, 5), (6, 5)])
    puzzle.add_renban([(7, 6), (8, 6), (8, 7)])
    puzzle.add_renban([(2, 2), (3, 2)])
    puzzle.add_renban([(0, 8), (1, 7)])
    puzzle.add_renban([(7, 0), (6, 0)])
    puzzle.add_renban([(7, 7), (6, 7)])
    puzzle.add_renban([(1, 6), (2, 6)])

    return puzzle
