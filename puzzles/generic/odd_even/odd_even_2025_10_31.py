"""PuzzleMadness Odd/Even Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Odd/Even Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/oddevensudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [1, 0, 0, 0, 8, 0, 0, 0, 0],
        [6, 0, 0, 1, 0, 0, 0, 0, 0],
        [3, 0, 9, 0, 0, 2, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_even_cell((0, 0))
    puzzle.add_odd_cell((0, 1))
    puzzle.add_even_cell((0, 2))
    puzzle.add_even_cell((0, 3))
    puzzle.add_even_cell((0, 4))
    puzzle.add_odd_cell((0, 5))
    puzzle.add_odd_cell((0, 6))
    puzzle.add_odd_cell((0, 7))
    puzzle.add_odd_cell((0, 8))
    puzzle.add_odd_cell((1, 0))
    puzzle.add_odd_cell((1, 1))
    puzzle.add_odd_cell((1, 2))
    puzzle.add_odd_cell((1, 3))
    puzzle.add_even_cell((1, 4))
    puzzle.add_odd_cell((1, 5))
    puzzle.add_even_cell((1, 6))
    puzzle.add_even_cell((1, 7))
    puzzle.add_even_cell((1, 8))
    puzzle.add_even_cell((2, 0))
    puzzle.add_odd_cell((2, 1))
    puzzle.add_even_cell((2, 2))
    puzzle.add_odd_cell((2, 3))
    puzzle.add_even_cell((2, 4))
    puzzle.add_odd_cell((2, 5))
    puzzle.add_even_cell((2, 6))
    puzzle.add_odd_cell((2, 7))
    puzzle.add_odd_cell((2, 8))
    puzzle.add_odd_cell((3, 0))
    puzzle.add_even_cell((3, 1))
    puzzle.add_odd_cell((3, 2))
    puzzle.add_even_cell((3, 3))
    puzzle.add_odd_cell((3, 4))
    puzzle.add_even_cell((3, 5))
    puzzle.add_even_cell((3, 6))
    puzzle.add_odd_cell((3, 7))
    puzzle.add_odd_cell((3, 8))
    puzzle.add_odd_cell((4, 0))
    puzzle.add_even_cell((4, 1))
    puzzle.add_even_cell((4, 2))
    puzzle.add_odd_cell((4, 3))
    puzzle.add_odd_cell((4, 4))
    puzzle.add_odd_cell((4, 5))
    puzzle.add_even_cell((4, 6))
    puzzle.add_even_cell((4, 7))
    puzzle.add_odd_cell((4, 8))
    puzzle.add_even_cell((5, 0))
    puzzle.add_odd_cell((5, 1))
    puzzle.add_odd_cell((5, 2))
    puzzle.add_odd_cell((5, 3))
    puzzle.add_even_cell((5, 4))
    puzzle.add_even_cell((5, 5))
    puzzle.add_odd_cell((5, 6))
    puzzle.add_odd_cell((5, 7))
    puzzle.add_even_cell((5, 8))
    puzzle.add_odd_cell((6, 0))
    puzzle.add_even_cell((6, 1))
    puzzle.add_odd_cell((6, 2))
    puzzle.add_even_cell((6, 3))
    puzzle.add_odd_cell((6, 4))
    puzzle.add_odd_cell((6, 5))
    puzzle.add_odd_cell((6, 6))
    puzzle.add_even_cell((6, 7))
    puzzle.add_even_cell((6, 8))
    puzzle.add_even_cell((7, 0))
    puzzle.add_odd_cell((7, 1))
    puzzle.add_even_cell((7, 2))
    puzzle.add_even_cell((7, 3))
    puzzle.add_odd_cell((7, 4))
    puzzle.add_even_cell((7, 5))
    puzzle.add_odd_cell((7, 6))
    puzzle.add_odd_cell((7, 7))
    puzzle.add_odd_cell((7, 8))
    puzzle.add_odd_cell((8, 0))
    puzzle.add_even_cell((8, 1))
    puzzle.add_odd_cell((8, 2))
    puzzle.add_odd_cell((8, 3))
    puzzle.add_odd_cell((8, 4))
    puzzle.add_even_cell((8, 5))
    puzzle.add_odd_cell((8, 6))
    puzzle.add_even_cell((8, 7))
    puzzle.add_even_cell((8, 8))

    return puzzle
