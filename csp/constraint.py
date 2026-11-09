
from abc import ABC, abstractmethod
from typing import Hashable

Variable = Hashable
Assignment = dict[Variable, int]
Domains = dict[Variable, set[int]]


class Constraint(ABC):
    def __init__(self, variables):
        self.variables = tuple(variables)

    @abstractmethod
    def is_satisfied(self, assignment: Assignment) -> bool:
        """Return False if an assignment violates this rule."""
        pass

    def propagate(self, domains: Domains) -> bool:
        """
        Remove impossible values from domains.
        Returns True if any domain changed.
        Raises ValueError if a contradiction is found.
        Default implementation performs no propagation.
        """
        return False
