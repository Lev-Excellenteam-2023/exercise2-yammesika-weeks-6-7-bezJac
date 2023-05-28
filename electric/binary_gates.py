from logic_gate import LogicGate
from abc import ABC, abstractmethod

"""
This module contains classes for implementing various Binary Gates.

Classes:

BinaryGate: Abstract class that represents all binary gates and inherits from the LogicGate class, which represents all
logic gates, both unary and binary gates.

Classes inheriting BinaryGate:
AndGate: Class for implementing the logical AND Gate. 
OrGate: Class for implementing the logical OR Gate.
NandGate: Class for implementing the logical NAND Gate.
NorGate: Class for implementing  the logical NOR Gate.
XorGate: Class for implementing the logical XOR Gate.

Each gate-specific class in this module has a method named output that returns the result of the logical
operation performed by the gate based on two input values.

All gate classes defined in this module are not meant to have instances, and only class-level objects can be created.
"""


class BinaryGate(LogicGate, ABC):

    @abstractmethod
    def output(input1 , input2):
        pass


class AndGate(BinaryGate):

    @staticmethod
    def output(input1, input2):
        return input1 and input2


class OrGate(BinaryGate):

    @staticmethod
    def output(input1, input2):
        return input1 or input2


class NandGate(BinaryGate):

    @staticmethod
    def output(input1, input2):
        return not(input1 and input2)


class NorGate(BinaryGate):

    @staticmethod
    def output(input1, input2):
        return not(input1 or input2)


class XorGate(BinaryGate):

    @staticmethod
    def output(input1, input2):
        return (input1 and not input2) or (not input1 and input2)