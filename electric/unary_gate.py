from logic_gate import LogicGate
from abc import ABC, abstractmethod

"""
This module contains classes for implementing unary Gates.

Classes:

UnaryGate: Abstract class that represents all unary gates and inherits from the LogicGate class, which represents all
logic gates, both unary and binary gates.

Classes inheriting BinaryGate:

Each gate-specific class in this module has a method named output that returns the result of the logical
operation performed by the gate based on two input values.

All gate classes defined in this module are not meant to have instances, and only class-level objects can be created.
"""


class UnaryGate(LogicGate, ABC):

    @abstractmethod
    def output(input1):
        pass


class NotGate(UnaryGate):

    @staticmethod
    def output(input1):
        return not input1
