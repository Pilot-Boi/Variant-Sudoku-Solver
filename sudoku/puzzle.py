from csp.solver import CSPSolver
from sudoku.constraints import (
    AllDifferentConstraint,
    ThermometerConstraint,
    KillerCageConstraint,
    NotEqualConstraint,
    NonConsecutiveConstraint,
    GermanWhispersConstraint,
    RenbanConstraint,
    generate_king_pairs,
    generate_knight_pairs,
    generate_orthogonal_pairs
)

class SudokuPuzzle:
    def __init__(self, grid):
        if len(grid) != 9 or any(len(row) != 9 for row in grid):
            raise ValueError("Grid must be 9x9")

        if any(
            not isinstance(value, int)
            or isinstance(value, bool)
            or value < 0
            or value > 9
            for row in grid
            for value in row
        ):
            raise ValueError("Cells must contain integers from 0 to 9")
        
        self.grid = [row.copy() for row in grid]
        
        self.variables = [
            (r, c)
            for r in range(9)
            for c in range(9)
        ]
        
        self.domains = {
            (r, c): set(range(1, 10))
            for r, c in self.variables
        }
        
        self.constraints = []
        self.add_standard_constraints()
        
    
    def add_standard_constraints(self):
        digits = set(range(1, 10))

        # Rows
        for r in range(9):
            cells = [(r, c) for c in range(9)]

            self.constraints.append(
                AllDifferentConstraint(
                    cells,
                    required_values=digits
                )
            )

        # Columns
        for c in range(9):
            cells = [(r, c) for r in range(9)]

            self.constraints.append(
                AllDifferentConstraint(
                    cells,
                    required_values=digits
                )
            )

        # 3x3 boxes
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                cells = [
                    (r, c)
                    for r in range(box_r, box_r + 3)
                    for c in range(box_c, box_c + 3)
                ]

                self.constraints.append(
                    AllDifferentConstraint(
                        cells,
                        required_values=digits
                    )
                )
    
    def add_diagonal_constraints(self):
        digits = set(range(1, 10))

        main_diagonal = [(i, i) for i in range(9)]
        anti_diagonal = [(i, 8 - i) for i in range(9)]

        self.add_constraint(
            AllDifferentConstraint(
                main_diagonal,
                required_values=digits
            )
        )

        self.add_constraint(
            AllDifferentConstraint(
                anti_diagonal,
                required_values=digits
            )
        )

    def add_anti_knight_constraints(self):
        """
        Add Anti-Knight Sudoku rules.

        Cells separated by a chess knight's move
        cannot contain the same digit.
        """
        for cell_a, cell_b in generate_knight_pairs():
            self.add_constraint(
                NotEqualConstraint(cell_a, cell_b)
            )
    
    def add_anti_king_constraints(self):
        """
        Enforce Anti-King Sudoku rules.

        Diagonally adjacent cells cannot contain
        the same digit.
        """
        for a, b in generate_king_pairs():
            self.add_constraint(NotEqualConstraint(a, b))
            
    
    def add_nonconsecutive_constraints(self):
        """
        Enforce global Nonconsecutive Sudoku rules.

        Orthogonally adjacent cells cannot contain
        consecutive digits.
        """
        for a, b in generate_orthogonal_pairs():
            self.add_constraint(
                NonConsecutiveConstraint(a, b)
            )
            
    def add_thermometer(self, cells):
        if len(cells) < 2:
            raise ValueError(
                "A thermometer must contain at least two cells."
            )

        if len(cells) > 9:
            raise ValueError(
                "A thermometer cannot exceed nine cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A thermometer cannot repeat a cell."
            )

        self.add_constraint(
            ThermometerConstraint(cells)
        )
        
    
    def add_killer_cage(self, cells, target_sum):
        """
        Add a Killer Sudoku cage.

        cells: list of (row, column) coordinates
        target_sum: required sum of the cage
        """
        if not cells:
            raise ValueError("Killer cage cannot be empty")

        if len(set(cells)) != len(cells):
            raise ValueError("Duplicate cage cells")

        if any(cell not in self.variables for cell in cells):
            raise ValueError("Invalid cage cell")

        self.add_constraint(
            KillerCageConstraint(cells, target_sum)
        )


    def add_german_whispers(self, cells):
        """
        Add a German Whispers line.

        cells: ordered list of (row, column) coordinates
        forming a connected path. Adjacent cells on the
        line must be orthogonally or diagonally adjacent
        on the grid.
        """
        cells = list(cells)

        if len(cells) < 2:
            raise ValueError(
                "A German Whispers line needs at least two cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A German Whispers line cannot repeat a cell."
            )

        if any(cell not in self.domains for cell in cells):
            raise ValueError(
                "German Whispers line references invalid cells."
            )

        for a, b in zip(cells, cells[1:]):
            dr = abs(a[0] - b[0])
            dc = abs(a[1] - b[1])

            if max(dr, dc) != 1:
                raise ValueError(
                    "German Whispers cells must be orthogonally "
                    "or diagonally adjacent."
                )

        self.add_constraint(
            GermanWhispersConstraint(cells)
        )


    def add_renban(self, cells):
        """
        Add a Renban line.

        cells: ordered list of (row, column) coordinates
        forming a connected path. Adjacent cells on the
        line must be orthogonally or diagonally adjacent
        on the grid.
        """
        cells = list(cells)

        if not 2 <= len(cells) <= 9:
            raise ValueError(
                "A Renban line needs between two and nine cells."
            )

        if len(set(cells)) != len(cells):
            raise ValueError(
                "A Renban line cannot repeat a cell."
            )

        if any(cell not in self.domains for cell in cells):
            raise ValueError(
                "Renban line references invalid cells."
            )

        for a, b in zip(cells, cells[1:]):
            dr = abs(a[0] - b[0])
            dc = abs(a[1] - b[1])

            if max(dr, dc) != 1:
                raise ValueError(
                    "Renban cells must be orthogonally "
                    "or diagonally adjacent."
                )

        self.add_constraint(
            RenbanConstraint(cells)
        )


    def add_constraint(self, constraint):
        if any(
            var not in self.domains
            for var in constraint.variables  
        ):
            raise ValueError("Constraint references invalid cells.")
        
        self.constraints.append(constraint)
    
    def check_uniqueness(self):
        """
        Determine whether the puzzle has exactly
        one solution.

        Returns:
            status: "none", "unique", or "multiple"
            solutions: up to two solution dictionaries
            solver: the solver used for the search
        """
        initial_assignment = {
            (r, c): self.grid[r][c]
            for r, c in self.variables
            if self.grid[r][c] != 0
        }

        solver = CSPSolver(
            self.variables,
            self.domains,
            self.constraints
        )

        solutions = solver.solve_all(
            initial_assignment,
            limit=2
        )

        if len(solutions) == 0:
            status = "none"
        elif len(solutions) == 1:
            status = "unique"
        else:
            status = "multiple"

        return status, solutions, solver
        
    def solve(self):
        initial_assignment = {
            (r, c): self.grid[r][c]
            for r, c in self.variables
            if self.grid[r][c] != 0
        }
            
        solver = CSPSolver(
            self.variables,
            self.domains,
            self.constraints,
        )
        
        solution = solver.solve(initial_assignment)
        
        return solution, solver
    
    @staticmethod
    def print_grid(assignment):
        if assignment is None:
            print("No solution found.")
            return
        
        for r in range(9):
            if r > 0 and r % 3 == 0 :
                print("------+-------+------")
                
            values = []
            
            for c in range(9):
                if c > 0 and c % 3 == 0:
                    values.append("|")
                    
                values.append(str(assignment[(r, c)]))
            print(" ".join(values))