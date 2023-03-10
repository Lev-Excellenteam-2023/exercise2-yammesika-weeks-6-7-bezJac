from abc import ABC, abstractmethod

"""
    Abstract base class for logic gates.

    Subclasses should implement the `output` method to compute the output
    of the logic gate given its inputs.
"""


class LogicGate(ABC):

    @abstractmethod
    def output(*args):
        pass
