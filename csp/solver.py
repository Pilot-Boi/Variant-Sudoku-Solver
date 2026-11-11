
from collections import defaultdict
from time import perf_counter

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
        self.instrument = False
        self.metrics = {}
        self._search_depth = 0
        self.reset_metrics()

    def reset_metrics(self):
        self.nodes = 0
        self.backtracks = 0
        self.propagation_rounds = 0
        self._search_depth = 0

        self.metrics = {
            "initial_candidates": 0,
            "initial_remaining_candidates": 0,
            "initial_candidates_eliminated": 0,
            "initial_propagation_seconds": 0.0,
            "total_propagation_seconds": 0.0,
            "candidates_eliminated": 0,
            "constraint_evaluations": 0,
            "constraint_reductions": 0,
            "constraint_checks": 0,
            "constraint_contradictions": 0,
            "validation_contradictions": 0,
            "max_search_depth": 0,
            "failed_branches": 0,
            "constraint_types": {},
        }
    
    def propagate(self, domains):
        """
        Propagate constraints until stable.

        Optionally collect detailed constraint statistics.
        """
        start_time = perf_counter() if self.instrument else None

        try:
            while True:
                self.propagation_rounds += 1
                changed = False

                for constraint in self.constraints:
                    if not self.instrument:
                        if constraint.propagate(domains):
                            changed = True
                        continue

                    name = type(constraint).__name__

                    stats = self.metrics["constraint_types"].setdefault(
                        name,
                        {
                            "evaluations": 0,
                            "reductions": 0,
                            "candidates_eliminated": 0,
                            "seconds": 0.0,
                            "contradictions": 0,
                            "validation_contradictions": 0,
                        },
                    )

                    # Measure only cells this constraint can change.
                    before = sum(
                        len(domains[var])
                        for var in constraint.variables
                    )

                    constraint_start = perf_counter()

                    try:
                        result = constraint.propagate(domains)

                    except ValueError:
                        stats["contradictions"] += 1
                        self.metrics["constraint_contradictions"] += 1
                        raise

                    finally:

                        elapsed = perf_counter() - constraint_start

                        after = sum(
                            len(domains[var])
                            for var in constraint.variables
                        )

                        eliminated = before - after

                        stats["evaluations"] += 1
                        stats["seconds"] += elapsed
                        stats["candidates_eliminated"] += eliminated

                        self.metrics["constraint_evaluations"] += 1
                        self.metrics["candidates_eliminated"] += eliminated

                        if eliminated > 0:
                            stats["reductions"] += 1
                            self.metrics["constraint_reductions"] += 1

                    if result:
                        changed = True

                if any(not values for values in domains.values()):
                    return False

                assignment = {
                    var: next(iter(values))
                    for var, values in domains.items()
                    if len(values) == 1
                }
                
                for constraint in self.constraints:
                    if self.instrument:
                        self.metrics["constraint_checks"] += 1

                    if not constraint.is_satisfied(assignment):
                        if self.instrument:
                            name = type(constraint).__name__

                            stats = self.metrics["constraint_types"].setdefault(
                                name,
                                {
                                    "evaluations": 0,
                                    "reductions": 0,
                                    "candidates_eliminated": 0,
                                    "seconds": 0.0,
                                    "contradictions": 0,
                                    "validation_contradictions": 0,
                                },
                            )

                            stats["validation_contradictions"] += 1
                            self.metrics["validation_contradictions"] += 1

                        return False

                if not changed:
                    return True

        except ValueError:
            return False

        finally:
            if self.instrument:
                self.metrics["total_propagation_seconds"] += (
                    perf_counter() - start_time
                )


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

    def backtrack(self, domains, depth=0):
        if self.instrument:
            self.metrics["max_search_depth"] = max(
                self.metrics["max_search_depth"], depth
            )

            if depth == 0:
                self.metrics["initial_candidates"] = sum(
                    len(values) for values in domains.values()
                )

                initial_start = perf_counter()

        propagated = self.propagate(domains)

        if self.instrument and depth == 0:
            self.metrics["initial_propagation_seconds"] = (
                perf_counter() - initial_start
            )

            remaining = sum(
                len(values) for values in domains.values()
            )

            self.metrics["initial_remaining_candidates"] = remaining

            self.metrics["initial_candidates_eliminated"] = (
                self.metrics["initial_candidates"] - remaining
            )

        if not propagated:
            self.backtracks += 1

            if self.instrument:
                self.metrics["failed_branches"] += 1

            return None

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

            if self.instrument:
                self.metrics["failed_branches"] += 1

            return None

        var = self.select_variable(domains)

        for value in sorted(domains[var]):
            self.nodes += 1

            new_domains = {
                v: values.copy()
                for v, values in domains.items()
            }

            new_domains[var] = {value}

            result = self.backtrack(new_domains, depth + 1)

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
        self.reset_metrics()

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
