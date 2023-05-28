from typing import Type, List, Union

from electric.logic_gate import LogicGate


class Connector:
    """
      Connects input gates to a gate that computes a logic operation.

      Attributes:
          gate (LogicGate): The gate that computes a logic operation.
          input_gates (list): The input gates connected to the gate.

      Methods:
          send_inputs: Computes the output of the gate given the inputs.
          calculate_output: Calculates the output of each input gate.
          count_gates: Counts the number of gates in a Connector or list of Connectors.

      """

    def __init__(self, gate: Type[LogicGate], input_gates: List[Union['Connector', Type[LogicGate]]]):
        """
        Initializes a Connector instance.

        Args:
            gate (Type[LogicGate]): The gate that computes a logic operation.
            input_gates (List[Union['Connector', Type[LogicGate']]):
                The input gates connected to the gate.
        """
        self.gate = gate
        self.input_gates = input_gates

    def send_inputs(self, inputs: List[bool]) -> bool:
        """
        Computes the output of the gate given the inputs.

        Args:
            inputs (list): The input values for the gate.

        Returns:
            The output value of the gate.
        """
        return self.gate.output(*self.calculate_input_gates_outputs(inputs))

    def calculate_input_gates_outputs(self, inputs: List[bool]) -> List[bool]:
        """
         Calculates the output from the input gates of the connector.
         if current input gate is a subclass of LogicGate, the specific amount of inputs is used
         for the current calculation, if it's a connector the amount of necessary inputs to be used is first calculated.

         Args:
             inputs (list): The logical input values to the input gates of the connector.

         Returns:
             A list containing the output values from the input gates.
         """
        result = []
        for index, current_gate in enumerate(self.input_gates):

            if isinstance(current_gate, Connector):
                count = self.logical_inputs_count(current_gate)
                result.append(current_gate.send_inputs(inputs[:count]))
                inputs = inputs[count:]

            elif current_gate.__name__ in ['OrGate', 'AndGate', 'NandGate', 'XorGate']:
                result.append(current_gate.output(inputs[0], inputs[1]))
                inputs = inputs[2:]

            else:
                result.append(current_gate.output(inputs[0]))
                inputs = inputs[1:]

        return result

    def logical_inputs_count(self, current: Union[
        'Connector', Type[LogicGate], List[Union['Connector', Type[LogicGate]]]]) -> int:
        """
        Recursively Count the number of logical inputs used in a logic circuit (Connector).

        Args:
            current: The current gate or connector being processed. It can be an instance of 'Connector',
                a subclass of 'LogicGate', or a list containing instances of 'Connector' or subclasses of 'LogicGate'.

        Returns:
            The number of logical inputs used in the circuit.
        """
        if not current:
            return 0

        if not isinstance(current, (Connector, list)):
            if current.__name__ == 'NotGate':
                return 1
            else:
                return 2

        if isinstance(current, list):
            return self.logical_inputs_count(current[0]) + self.logical_inputs_count(current[1:])
        else:
            return current.logical_inputs_count(current.input_gates[0]) + current.logical_inputs_count(
                current.input_gates[1:])
