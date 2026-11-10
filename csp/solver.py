
from collections import defaultdict, deque


class CSPSolver:
    def __init__(self, variables, domains, constraints):
        self.variables = list(variables)
        self.domains = {
            var: set(domains[var])
            for var in self.variables
        }
        self.constraints = list(constraints)

        self.constraints_by_variable = defaultdict(list)

        for constraint in self.constraints:
            for var in constraint.variables:
                self.constraints_by_variable[var].append(constraint)

        self.nodes = 0
        self.backtracks = 0
        self.propagation_rounds = 0

    def propagate(self, domains):
        """
        Repeatedly propagate all constraints until
        no more candidates can be eliminated.

        Returns False if a contradiction occurs.
        """
        try:
            while True:
                self.propagation_rounds += 1
                changed = False

                for constraint in self.constraints:
                    if constraint.propagate(domains):
                        changed = True

                if any(not values for values in domains.values()):
                    return False

                # Singleton domains are forced assignments.
                assignment = {
                    var: next(iter(values))
                    for var, values in domains.items()
                    if len(values) == 1
                }

                if not all(
                    constraint.is_satisfied(assignment)
                    for constraint in self.constraints
                ):
                    return False

                if not changed:
                    return True

        except ValueError:
            return False

    def select_variable(self, domains):
        """
        MRV: choose the unassigned variable with
        the smallest remaining domain.
        """
        unassigned = [
            var for var in self.variables
            if len(domains[var]) > 1
        ]

        return min(
            unassigned,
            key=lambda var: len(domains[var])
        )

    def backtrack(self, domains):
        # First, propagate every constraint.
        if not self.propagate(domains):
            self.backtracks += 1
            return None

        # All variables have been forced to one value.
        if all(len(domains[var]) == 1 for var in self.variables):
            solution = {
                var: next(iter(domains[var]))
                for var in self.variables
            }

            if all(
                constraint.is_satisfied(solution)
                for constraint in self.constraints
            ):
                return solution

            self.backtracks += 1
            return None

        var = self.select_variable(domains)

        for value in sorted(domains[var]):
            self.nodes += 1

            # Copy domains so failed branches
            # cannot affect other branches.
            new_domains = {
                v: values.copy()
                for v, values in domains.items()
            }

            new_domains[var] = {value}

            result = self.backtrack(new_domains)

            if result is not None:
                return result

        self.backtracks += 1
        return None
    
    
    def backtrack_all(self, domains, solutions, limit):
        """
        Search for multiple solutions.

        Stops when the requested number of solutions
        has been found.
        """
        if len(solutions) >= limit:
            return

        if not self.propagate(domains):
            self.backtracks += 1
            return

        # Check whether every variable is assigned.
        if all(
            len(domains[var]) == 1
            for var in self.variables
        ):
            solution = {
                var: next(iter(domains[var]))
                for var in self.variables
            }

            if all(
                constraint.is_satisfied(solution)
                for constraint in self.constraints
            ):
                solutions.append(solution)
            else:
                self.backtracks += 1

            return

        var = self.select_variable(domains)

        for value in sorted(domains[var]):
            if len(solutions) >= limit:
                return

            self.nodes += 1

            new_domains = {
                v: values.copy()
                for v, values in domains.items()
            }

            new_domains[var] = {value}

            self.backtrack_all(
                new_domains, solutions, limit
            )

        self.backtracks += 1

    def solve_all(self, initial_assignment=None, limit=2):
        """
        Find up to 'limit' solutions.

        Returns a list of solution dictionaries.
        """
        if limit < 1:
            raise ValueError("Solution limit must be >= 1")

        self.nodes = 0
        self.backtracks = 0
        self.propagation_rounds = 0

        domains = {
            var: values.copy()
            for var, values in self.domains.items()
        }

        initial_assignment = initial_assignment or {}

        for var, value in initial_assignment.items():
            if var not in domains or value not in domains[var]:
                return []

            domains[var] = {value}

        solutions = []

        self.backtrack_all(domains, solutions, limit)

        return solutions

    def solve(self, initial_assignment=None):
        self.nodes = 0
        self.backtracks = 0
        self.propagation_rounds = 0

        domains = {
            var: values.copy()
            for var, values in self.domains.items()
        }

        initial_assignment = initial_assignment or {}

        for var, value in initial_assignment.items():
            if var not in domains or value not in domains[var]:
                return None

            domains[var] = {value}

        return self.backtrack(domains)