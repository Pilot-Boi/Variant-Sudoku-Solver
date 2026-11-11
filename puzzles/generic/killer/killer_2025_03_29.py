"""PuzzleMadness Killer Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Killer Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/killersudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_killer_cage([(8, 0), (8, 1), (8, 2)], 18)
    puzzle.add_killer_cage([(0, 0), (0, 1)], 11)
    puzzle.add_killer_cage([(1, 0), (1, 1), (2, 0)], 17)
    puzzle.add_killer_cage([(3, 0), (4, 0), (5, 0)], 16)
    puzzle.add_killer_cage([(0, 2), (0, 3)], 4)
    puzzle.add_killer_cage([(0, 4), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)], 23)
    puzzle.add_killer_cage([(0, 5), (0, 6)], 13)
    puzzle.add_killer_cage([(0, 7), (0, 8)], 15)
    puzzle.add_killer_cage([(1, 7), (1, 8), (2, 8)], 18)
    puzzle.add_killer_cage([(2, 7), (3, 7), (4, 7)], 13)
    puzzle.add_killer_cage([(3, 8), (4, 8), (5, 8)], 12)
    puzzle.add_killer_cage([(6, 6), (6, 7), (6, 8)], 20)
    puzzle.add_killer_cage([(7, 6), (7, 7), (7, 8)], 11)
    puzzle.add_killer_cage([(8, 6), (8, 7), (8, 8)], 14)
    puzzle.add_killer_cage([(2, 1), (3, 1), (4, 1)], 19)
    puzzle.add_killer_cage([(2, 2), (2, 3), (3, 2)], 15)
    puzzle.add_killer_cage([(3, 3), (4, 2), (4, 3)], 7)
    puzzle.add_killer_cage([(5, 1), (5, 2), (5, 3)], 21)
    puzzle.add_killer_cage([(2, 4), (3, 4)], 4)
    puzzle.add_killer_cage([(2, 5), (2, 6), (3, 6)], 20)
    puzzle.add_killer_cage([(3, 5), (4, 5), (4, 6)], 16)
    puzzle.add_killer_cage([(5, 5), (5, 6), (5, 7)], 11)
    puzzle.add_killer_cage([(4, 4), (5, 4), (6, 4), (7, 4), (8, 4)], 35)
    puzzle.add_killer_cage([(6, 5), (7, 5), (8, 5)], 8)
    puzzle.add_killer_cage([(6, 3), (7, 3), (8, 3)], 17)
    puzzle.add_killer_cage([(6, 0), (6, 1), (6, 2)], 13)
    puzzle.add_killer_cage([(7, 0), (7, 1), (7, 2)], 14)

    return puzzle
